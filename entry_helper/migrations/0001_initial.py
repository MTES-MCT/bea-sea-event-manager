# Generated by Django 3.2.13 on 2022-05-16 07:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_number', models.TextField()),
                ('name', models.TextField()),
                ('imo_number', models.TextField(null=True)),
                ('national_id', models.TextField(null=True)),
                ('declarative_entity', models.TextField()),
                ('event_location', models.TextField()),
                ('event_datetime', models.DateTimeField()),
                ('event_type', models.TextField()),
            ],
        ),
    ]
