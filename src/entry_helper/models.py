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

    def __str__(self):
        return self.report_number