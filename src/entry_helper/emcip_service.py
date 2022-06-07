import os
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

import requests
from django.conf import settings

from entry_helper.models import Report

OCCURRENCE_ENDPOINT = "occurrence"


@dataclass
class EmcipAttribute:
    nodes_breadcrumb: list
    code: str

attribute_mapping_config = {
    "occurrence_date": EmcipAttribute(
        nodes_breadcrumb = ["TE-28"],
        code = "TA-346",
    )
}


class BEAToEmcipService:
    def __init__(self):
        self.shared_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {settings.BASIC_AUTHORIZATION_TOKEN}",
        }
        self.occurrence_endpoint_url = os.path.join(settings.EMCIP_URL, OCCURRENCE_ENDPOINT)

    def push_report_to_emcip(self, report: Report) -> None:
        occurrence = self._format_report_values_for_emcip(report)
        print("occurrence", occurrence)
        self._post_occurrence(occurrence, self.shared_headers)

    def _format_report_values_for_emcip(self, report: Report) -> dict:

        def get_occurrence_date(date_format: str = "%Y-%m-%dT%H:%M"):
            return datetime.strftime(report.event_datetime, date_format)

        return {
            "occurrence_date": get_occurrence_date()
        }

    def _post_occurrence(self, body: dict, headers: dict) -> None:
        response = requests.post(self.occurrence_endpoint_url, json=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Push to emcip failed with status_code: {response.status_code}")


class EmcipQueryBodyBuilder:
    def __init__(self, attribute_mapping: dict):
        self.body = self._build_empty_body()
        self.existing_nodes = {}
        self.attribute_mapping = attribute_mapping

    def _build_empty_body(self) -> dict:
        return {
            "nodes": [],
            "attributes": [],
        }

    def build(self, occurrence: dict) -> dict:
        for attribute_name, attribute_value in occurrence.items():
            self._add_attribute_to_body(attribute_name, attribute_value)
        return self.body

    def _add_attribute_to_body(self, attribute_name: str, attribute_value: str) -> dict:
            emcip_attribute = self.attribute_mapping[attribute_name]
            self._add_missing_nodes(emcip_attribute.nodes_breadcrumb)
            self._add_attribute(emcip_attribute, attribute_value)

    def _add_missing_nodes(self, nodes: list) -> None:
        """
        Returns
        """
        parent_node_uuid = None
        for node in nodes:
            if node not in self.existing_nodes:
                current_node_uuid = str(uuid4())
                self.existing_nodes[node] = current_node_uuid
                self.body["nodes"].append(
                    {
                        "uuid": current_node_uuid,
                        "parentUuid": parent_node_uuid,
                        "taxonomyEntityIdCode": node,
                    }
                )
            parent_node_uuid = self.existing_nodes[node]
        return parent_node_uuid

    def _get_parent_node_uuid(self, attribute: EmcipAttribute) -> str:
        return self.existing_nodes[attribute.nodes_breadcrumb[-1]]

    def _add_attribute(self, attribute: EmcipAttribute, value: str) -> None:
        self.body["attributes"].append(
            {
                "nodeUuid": self._get_parent_node_uuid(attribute),
                "taxonomyEntityIdCode": attribute.code,
                "value": value,
                "taxonomyCodeIdCode": None,
            }
        )
