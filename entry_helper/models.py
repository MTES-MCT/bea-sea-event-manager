from uuid import uuid4

from django.db import models


class Report(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    report_number = models.TextField()
    name = models.TextField()
    imo_number = models.TextField(null=True)
    national_id = models.TextField(null=True)
    declarative_entity = models.TextField()
    event_location = models.TextField()
    event_datetime = models.DateTimeField()
    event_type = models.TextField()

    def __str__(self):
        return self.report_number
