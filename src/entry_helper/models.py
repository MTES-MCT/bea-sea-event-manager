from datetime import datetime
from uuid import uuid4

from django.db import models


class Report(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    report_number = models.TextField()
    ship_name = models.TextField(null=True)
    imo_number = models.TextField(null=True)
    registration_number = models.TextField(null=True)
    declarative_entity = models.TextField()
    event_location = models.TextField()
    event_datetime = models.DateTimeField()
    event_type = models.TextField()
    ship_total_length = models.FloatField(null=True)
    ship_type = models.TextField(null=True)
    nb_deceased = models.IntegerField()
    nb_lost = models.IntegerField()
    nb_injured = models.IntegerField()
    status = models.TextField(default="todo")

    @classmethod
    def from_raw_report(cls, raw_report: dict[str, str]) -> "Report":
        try:
            return cls(
                report_number=raw_report.get("sitrep_num"),
                ship_name=raw_report.get("ship_name", None),
                imo_number=raw_report.get("imo_number", None),
                registration_number=raw_report.get("ship_immat", None),
                declarative_entity=raw_report.get("declarative_entity"),
                event_location=raw_report.get("event_location"),
                event_datetime=raw_report.get("event_date"),
                event_type=raw_report.get("event_type"),
                ship_total_length=raw_report.get("ship_total_length", None),
                ship_type=raw_report.get("ship_type", None),
                nb_deceased=int(raw_report.get("nb_deceased")),
                nb_lost=int(raw_report.get("nb_lost")),
                nb_injured=int(raw_report.get("nb_injured")),
            )
        except KeyError as e:
            raise ValueError(f"Missing key in raw report: {e}")

    def __str__(self):
        return self.report_number
