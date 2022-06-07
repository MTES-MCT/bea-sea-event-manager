from datetime import datetime
from unittest.mock import patch

from django.test import TestCase

from entry_helper.models import Report
from entry_helper.core import switch_report_to_done

class TestTests(TestCase):
    def test_tests_are_working(self):
        assert True


class TestSitrepHandling(TestCase):
    def setUp(self) -> None:
        self.report = Report(
            report_number="test_report_number",
            ship_name="test_ship_name",
            imo_number="test_imo_number",
            registration_number="test_registration_number",
            declarative_entity="test_declarative_entity",
            event_location="test_event_location",
            event_datetime=datetime(2020, 1, 1, 0, 0),
            event_type="test_event_type",
            ship_total_length=1.0,
            ship_type="test_ship_type",
            nb_deceased=1,
            nb_lost=2,
            nb_injured=3,
            status="todo",
        )
        self.report.save()
    
    def tearDown(self) -> None:
        Report.objects.all().delete()

    @patch("entry_helper.core.BEAToEmcipService.push_report_to_emcip")
    def test_sitrep_switch_from_todo_to_done(self, mock_push_service):
        self.assertEqual(self.report.status, "todo")

        switch_report_to_done(self.report)

        updated_report = Report.objects.get(uuid=self.report.uuid)

        self.assertEqual(updated_report.uuid, self.report.uuid)
        self.assertEqual(updated_report.status, "done")

        mock_push_service.assert_called_with(updated_report)
