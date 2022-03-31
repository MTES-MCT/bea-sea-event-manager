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


@pytest.mark.parametrize("index", [0, 1])
def test_get_sea_event_by_uuid(initial_sea_events_persisted_data, index):
    raw_sea_event = initial_sea_events_persisted_data[index]
    expected_sea_event = SeaEvent(
        uuid=raw_sea_event["uuid"],
        label=raw_sea_event["label"],
        type=raw_sea_event["type"],
        date=raw_sea_event["date"],
        time=raw_sea_event["time"],
        cross_entity=raw_sea_event["crossEntity"],
        sitrep_number=raw_sea_event["sitrepNumber"],
        region=raw_sea_event["region"],
        ship_type=raw_sea_event["shipType"],
        imo_number=raw_sea_event["imoNumber"],
        immat_number=raw_sea_event["immatNumber"],
        lht=raw_sea_event["lht"],
        casualty_number=raw_sea_event["casualtyNumber"],
        missing_number=raw_sea_event["missingNumber"],
        injured_number=raw_sea_event["injuredNumber"],
    )

    sea_event = sea_events_repository.get_by_uuid(expected_sea_event.uuid)

    assert sea_event == expected_sea_event


def test_get_sea_event_missing_uuid():
    missing_uuid = "missing-uuid"
    missing_sea_event = sea_events_repository.get_by_uuid(missing_uuid)

    assert missing_sea_event is None
