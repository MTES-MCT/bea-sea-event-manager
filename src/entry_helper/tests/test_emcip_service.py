from unittest.mock import patch

from django.test import TestCase

from entry_helper.emcip_service import EmcipQueryBodyBuilder, EmcipAttribute



@patch("entry_helper.emcip_service.uuid4", side_effect=[
    "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
    "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
    "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
])
class TestQueryBodyBuilder(TestCase):
    def test_query_builder_is_working_for_a_single_root_attribute(self, mock_uuid):
        self.maxDiff = None
        occurrence = {
            "occurrence_date": "2020-01-01T00:00",
        }
        test_attribute_mapping = {
            "occurrence_date": EmcipAttribute(
                nodes_breadcrumb = ["TE-28"],
                code = "TA-346",
            )
        }

        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": 'TE-28',
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TA-346" ,
                    "value": occurrence["occurrence_date"],
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipQueryBodyBuilder(attribute_mapping=test_attribute_mapping).build(occurrence)

        self.assertEqual(body, expected_body)

    def test_query_builder_is_working_for_a_nested_attribute(self, mock_uuid):
        self.maxDiff = None
        occurrence = {
            "occurrence_date": "2020-01-01T00:00",
        }
        test_attribute_mapping = {
            "occurrence_date": EmcipAttribute(
                nodes_breadcrumb = ["TE-28", "TE-24"],
                code = "TA-346",
            )
        }

        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": 'TE-28',
                },
                {
                    "uuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": 'TE-24',
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TA-346" ,
                    "value": occurrence["occurrence_date"],
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipQueryBodyBuilder(attribute_mapping=test_attribute_mapping).build(occurrence)

        self.assertEqual(body, expected_body)

    def test_query_builder_is_working_for_2_attribute_with_related_nodes(self, mock_uuid):
        self.maxDiff = None
        occurrence = {
            "occurrence_date": "2020-01-01T00:00",
            "occurrence_location": "test location",
        }
        test_attribute_mapping = {
            "occurrence_date": EmcipAttribute(
                nodes_breadcrumb = ["TE-28", "TE-24"],
                code = "TA-346",
            ),
            "occurrence_location": EmcipAttribute(
                nodes_breadcrumb = ["TE-28", "TE-24", "TE-25"],
                code = "TA-347",
            ),
        }

        expected_body = {
            "nodes": [
                {
                    "uuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": None,
                    "taxonomyEntityIdCode": 'TE-28',
                },
                {
                    "uuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "b8d9f8f0-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": 'TE-24',
                },
                {
                    "uuid": "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
                    "parentUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": 'TE-25',
                },
            ],
            "attributes": [
                {
                    "nodeUuid": "c8d9f8f1-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TA-346" ,
                    "value": occurrence["occurrence_date"],
                    "taxonomyCodeIdCode": None,
                },
                {
                    "nodeUuid": "d8d9f8f2-f8e9-11ea-b3de-0242ac130004",
                    "taxonomyEntityIdCode": "TA-347" ,
                    "value": occurrence["occurrence_location"],
                    "taxonomyCodeIdCode": None,
                },
            ],
        }

        body = EmcipQueryBodyBuilder(attribute_mapping=test_attribute_mapping).build(occurrence)

        self.assertEqual(body, expected_body)
