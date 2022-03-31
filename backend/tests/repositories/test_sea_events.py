from copy import deepcopy

import pytest

from src.io.repositories import sea_events_repository
from src.entities import SeaEvent


def _set_repository_data(repository_data: list[dict]):
    sea_events_repository._sea_events = deepcopy(repository_data)


def _reset_repository():
    sea_events_repository._sea_events = []


@pytest.fixture()
def initial_sea_events_persisted_data(dataset_sea_events_as_dict):
    initial_data = dataset_sea_events_as_dict["sea-events-1"]
    _set_repository_data(initial_data)
    yield initial_data
    _reset_repository()


def test_get_all(initial_sea_events_persisted_data):
    expected_sea_events = [
        SeaEvent(
            uuid=sea_event["uuid"],
            ship_name=sea_event["shipName"],
            event_type=sea_event["eventType"],
            occurrence_date=sea_event["occurrenceDate"],
            occurrence_time=sea_event["occurrenceTime"],
            occurrence_national_id=sea_event["occurrenceNationalId"],
            notification_entity=sea_event["notificationEntity"],
            registry_number=sea_event["registryNumber"],
            imo=sea_event["IMO"],
            occurrence_sea_area=sea_event["occurrenceSeaArea"],
            ship_type=sea_event["shipType"],
            overall_length=sea_event["overallLength"],
            nb_lives_lost=sea_event["nbLivesLost"],
            nb_injured_people=sea_event["nbInjuredPeople"],
            nb_missing_people=sea_event["nbMissingPeople"],
        )
        for sea_event in initial_sea_events_persisted_data
    ]

    all_sea_events = sea_events_repository.get_all()

    assert len(all_sea_events) == len(expected_sea_events)
    for sea_event in all_sea_events:
        assert sea_event in expected_sea_events


def test_get_all_no_sea_events():
    expected_sea_events = []

    all_sea_events = sea_events_repository.get_all()

    assert all_sea_events == expected_sea_events
