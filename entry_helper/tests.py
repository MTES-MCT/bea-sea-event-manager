from datetime import datetime

from django.test import TestCase

from entry_helper.models import Report
from entry_helper.internals import switch_report_to_done

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
            status="todo",
        )
        self.report.save()
    
    def tearDown(self) -> None:
        Report.objects.all().delete()

    def test_sitrep_switch_from_todo_to_done(self):
        self.assertEqual(self.report.status, "todo")

        switch_report_to_done(self.report)

        updated_report = Report.objects.get(uuid=self.report.uuid)

        self.assertEqual(updated_report.uuid, self.report.uuid)
        self.assertEqual(updated_report.status, "done")
