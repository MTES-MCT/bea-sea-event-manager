from unittest.mock import patch

from django.test import TestCase

from entry_helper.services.emcip import EmcipBody, AttributeMapping, Occurrence


@patch(
    "entry_helper.services.emcip.uuid4",
    side_effect=[
        "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
        "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
        "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
    ],
)
class TestQueryBodyBuilder(TestCase):
    def test_query_builder_is_working_for_a_single_root_attribute(self, mock_uuid):
        self.maxDiff = None
        occurrence = Occurrence(
            occurrence_date="2020-01-01T00:00",
        )
        test_attribute_mapping = AttributeMapping.from_dict(
            {
                "occurrence_date": {
                    "nodes_breadcrumb": ["TE-28"],
                    "code": "TA-346",
                }
            }
        )
        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": "TE-28",
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyAttributeIdCode": "TA-346",
                    "value": occurrence.occurrence_date,
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipBody.from_occurrence(occurrence, test_attribute_mapping)

        self.assertEqual(body.to_json(), expected_body)

    def test_query_builder_is_working_for_a_nested_attribute(self, mock_uuid):
        self.maxDiff = None
        occurrence = Occurrence(
            occurrence_date="2020-01-01T00:00",
        )
        test_attribute_mapping = AttributeMapping.from_dict(
            {
                "occurrence_date": {
                    "nodes_breadcrumb": ["TE-28", "TE-24"],
                    "code": "TA-346",
                }
            }
        )
        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": "TE-28",
                },
                {
                    "uuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TE-24",
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyAttributeIdCode": "TA-346",
                    "value": occurrence.occurrence_date,
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipBody.from_occurrence(occurrence, test_attribute_mapping)

        self.assertEqual(body.to_json(), expected_body)

    def test_query_builder_is_working_for_2_attribute_with_related_nodes(
        self, mock_uuid
    ):
        self.maxDiff = None
        occurrence = Occurrence(
            occurrence_date="2020-01-01T00:00",
            occurrence_location="test location",
        )
        test_attribute_mapping = AttributeMapping.from_dict(
            {
                "occurrence_date": {
                    "nodes_breadcrumb": ["TE-28", "TE-24"],
                    "code": "TA-346",
                },
                "occurrence_location": {
                    "nodes_breadcrumb": ["TE-28", "TE-24", "TE-25"],
                    "code": "TA-347",
                },
            }
        )
        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": "TE-28",
                },
                {
                    "uuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TE-24",
                },
                {
                    "uuid": "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TE-25",
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyAttributeIdCode": "TA-346",
                    "value": occurrence.occurrence_date,
                    "taxonomyCodeIdCode": None,
                },
                {
                    "nodeUuid": "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyAttributeIdCode": "TA-347",
                    "value": occurrence.occurrence_location,
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipBody.from_occurrence(occurrence, test_attribute_mapping)

        self.assertEqual(body.to_json(), expected_body)

    def test_query_builder_is_validating_if_a_regex_is_given(self, mock_uuid):
        self.maxDiff = None
        regex = "^[12][901][0-9][0-9]-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T00:00Z$"
        valid_occurrence = Occurrence(
            occurrence_date="2020-01-01T00:00Z",
        )
        invalid_occurrence = Occurrence(
            occurrence_date="2020-01-01T23:43Z"
        )
        test_attribute_mapping = AttributeMapping.from_dict(
            {
                "occurrence_date": {
                    "nodes_breadcrumb": ["TE-28", "TE-24"],
                    "code": "TA-346",
                    "regex": regex
                },
            }
        )

        EmcipBody.from_occurrence(valid_occurrence, test_attribute_mapping)

        with self.assertRaises(ValueError) as e:
            EmcipBody.from_occurrence(invalid_occurrence, test_attribute_mapping)

        self.assertIn(invalid_occurrence.occurrence_date, str(e.exception))
        self.assertIn(regex, str(e.exception))
