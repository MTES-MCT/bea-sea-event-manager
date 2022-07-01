import os
import re
from dataclasses import dataclass, asdict
from pprint import pprint
from typing import Any
from uuid import uuid4

import requests
from django.conf import settings

from entry_helper.models import Report
from entry_helper.exceptions import FailedPushToEmcip

OCCURRENCE_ENDPOINT = "occurrence"


@dataclass
class Attribute:
    """
    An attribute is the description of an attribute as per EMCIP definition

    it is composed of:
    - A node breadcrumb which relate in EMCIP interface to group of attributes.
    - A unique code for EMCIP to match the corresponding attribute
    - An optionnal validation regex to limit bad API calls (this should be at least the regex used in EMCIP taxonomy)
    """
    nodes_breadcrumb: list
    code: str
    regex: str | None

    @classmethod
    def from_raw_content(
        cls, nodes_breadcrumb: list[str], code: str, regex: str
    ) -> "Attribute":
        """
        Build new Attribute based on its explicit fields.
        """
        return cls(
            nodes_breadcrumb=nodes_breadcrumb,
            code=code,
            regex=regex,
        )


class AttributeMapping:
    @classmethod
    def from_dict(cls, attribute_mapping_config: dict[str, dict]) -> "AttributeMapping":
        """
        Create an arbitrary AttributeMapping instance from a dictionary
        :Note: attributes are not validated nor pre defined, so it's up to the user to provide valid fields

        Example of attribute mapping dictionnary:
        {
            "occurrence_date": {
                "nodes_breadcrumb": ["TE-28"],
                "code": "TA-346",
                "regex: "^[12][901][0-9][0-9]-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T00:00Z$",
            }
        }
        values of nodes_breadcrumb are a list in descending order
        => the first node to the left is the top node of the node tree)
        """
        attribute_mapping = cls()
        for attribute_name, attribute_config in attribute_mapping_config.items():
            setattr(
                attribute_mapping,
                attribute_name,
                Attribute.from_raw_content(
                    nodes_breadcrumb=attribute_config["nodes_breadcrumb"],
                    code=attribute_config["code"],
                    regex=attribute_config.get("regex", None),
                ),
            )
        return attribute_mapping


@dataclass
class Occurrence:
    """
    An occurrence is a data transport object carrying values formatted for EMCIP.

    it is used as a clean support to generate generative queries into EMCIP.
    Every attribute is optionnal because data can be missing and the goal of the
    app is to provide "as many informations as possible" not "at least some informations".
    """
    occurrence_date: str = None
    occurrence_location: str = None

    @classmethod
    def from_report(cls, report: Report) -> "Occurrence":
        """Based on a Report, build a valid Occurrence at both EMCIP and BEA expected format."""
        occurrence_date = (
            report.event_datetime.strftime("%Y-%m-%dT00:00Z")
            if report.event_datetime
            else None
        )
        occurrence_location = report.event_location if report.event_location else None
        return cls(
            occurrence_date=occurrence_date, occurrence_location=occurrence_location
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Export an occurrence as a dict containing non null attribute values.
        """
        raw_occurrence_dict = asdict(self)
        return {
            attribute_name: attribute_value
            for attribute_name, attribute_value in raw_occurrence_dict.items()
            if attribute_value is not None
        }


class EmcipBody:
    """
    An EmcipBody is a complex object gathering necessary data to build the body
    of a query used in EMCIP API.

    It requires an AttributeMapping in order to perform on demand body formatting.

    It should always be build based on an Occurrence through from_occurrence factory method!
    """
    def __init__(self, attribute_mapping: AttributeMapping) -> None:
        self.attribute_mapping = attribute_mapping
        self.nodes: list[dict] = []
        self.attributes: list[dict] = []
        self.existing_nodes: dict[str, str] = {}

    @classmethod
    def from_occurrence(
        cls, occurrence: Occurrence, attribute_mapping: AttributeMapping
    ) -> "EmcipBody":
        """
        Based on an Occurrence and an AttributeMapping,
        build a valid body for EMCIP API.
        """
        body = cls(attribute_mapping=attribute_mapping)
        for attribute_name, attribute_value in occurrence.to_dict().items():
            body._build_attribute(attribute_name, attribute_value)
        return body

    def to_json(self) -> dict[str, list]:
        """
        Format the EmcipBody as a json-like dictionnary ready to be used in a
        call to the API "As Is".
        """
        return {
            "nodes": self.nodes,
            "attributes": self.attributes,
        }

    def _build_attribute(self, attribute_name: str, attribute_value: str) -> None:
        emcip_attribute_config: Attribute = getattr(
            self.attribute_mapping, attribute_name
        )
        if emcip_attribute_config is None:
            return

        self._validate_value(emcip_attribute_config, attribute_value)
        self._add_missing_nodes(emcip_attribute_config.nodes_breadcrumb)
        self._add_attribute(emcip_attribute_config, attribute_value)

    def _add_missing_nodes(self, node_codes: list[str]) -> None:
        parent_node_uuid = None
        for node_code in node_codes:
            if node_code not in self.existing_nodes:
                current_node_uuid = str(uuid4())
                self.existing_nodes[node_code] = current_node_uuid
                self.nodes.append(
                    {
                        "uuid": current_node_uuid,
                        "parentUuid": parent_node_uuid,
                        "taxonomyEntityIdCode": node_code,
                    }
                )
            parent_node_uuid = self.existing_nodes[node_code]
        return parent_node_uuid

    def _validate_value(self, attribute_config: Attribute, attribute_value: str) -> None:
        if attribute_config.regex and not re.match(attribute_config.regex, attribute_value):
            raise ValueError(f"{attribute_value} did not match {attribute_config.regex}")

    def _add_attribute(
        self, attribute_config: Attribute, attribute_value: str
    ) -> None:
        self.attributes.append(
            {
                "nodeUuid": self._get_parent_node_uuid(attribute_config),
                "taxonomyAttributeIdCode": attribute_config.code,
                "value": attribute_value,
                "taxonomyCodeIdCode": None,
            }
        )

    def _get_parent_node_uuid(self, attribute_config: Attribute) -> str:
        parent_node_code = attribute_config.nodes_breadcrumb[-1]
        return self.existing_nodes[parent_node_code]


class BEAToEmcipService:
    """
    A service able to interoperate french maritime incident reports with european
    maritime incident reports in EMCIP.

    It requires to be configured with an AttributeMapping in order to be able
    to properly push the data into EMCIP system.
    """
    def __init__(self, attributes_mapping: AttributeMapping) -> None:
        self.shared_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {settings.BASIC_AUTHORIZATION_TOKEN}",
        }
        self.occurrence_endpoint_url = os.path.join(
            settings.EMCIP_URL, OCCURRENCE_ENDPOINT
        )
        self.attribute_mapping = attributes_mapping

    def push_report_to_emcip(self, report: Report) -> None:
        """
        Push a Report into Emcip
        """
        occurrence = Occurrence.from_report(report)
        self._post_occurrence(occurrence, self.shared_headers)

    def _post_occurrence(self, occurrence: Occurrence, headers: dict) -> None:
        body = EmcipBody.from_occurrence(occurrence, self.attribute_mapping).to_json()
        response = requests.post(
            self.occurrence_endpoint_url, json=body, headers=headers
        )

        print("body")
        pprint(body)
        print(response.content)
        pprint(response.json())

        if response.status_code != 200:
            raise FailedPushToEmcip(response.status_code, response.reason)
