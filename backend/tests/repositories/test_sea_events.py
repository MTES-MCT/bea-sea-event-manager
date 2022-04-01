from copy import deepcopy

import pytest

from src.io.repositories import sea_events_repository
from src.entities import SeaEvent


@pytest.fixture()
def initial_sea_events_persisted_data(dataset_sea_events_as_dict):
    initial_data = dataset_sea_events_as_dict["sea-events-1"]
    _set_repository_data(initial_data)
    yield initial_data
    _reset_repository()


def test_get_all(initial_sea_events_persisted_data):
    expected_sea_events = [
        _sea_event_from_internal_representation(sea_event)
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
    expected_sea_event = _sea_event_from_internal_representation(raw_sea_event)

    sea_event = sea_events_repository.get_by_uuid(expected_sea_event.uuid)

    assert sea_event == expected_sea_event


def test_get_sea_event_missing_uuid():
    missing_uuid = "missing-uuid"
    missing_sea_event = sea_events_repository.get_by_uuid(missing_uuid)

    assert missing_sea_event is None


def _set_repository_data(repository_data: list[dict]):
    sea_events_repository._sea_events = deepcopy(repository_data)


def _reset_repository():
    sea_events_repository._sea_events = []


def _sea_event_from_internal_representation(sea_event: dict):
    return SeaEvent(
        uuid=sea_event["uuid"],
        ship_name=sea_event["shipName"],
        event_type=sea_event["eventType"],
        occurrence_date=sea_event["occurrenceDate"],
        occurrence_time=sea_event["occurrenceTime"],
        occurrence_national_id=sea_event["occurrenceNationalId"],
        notification_date=sea_event["notificationDate"],
        notification_time=sea_event["notificationTime"],
        notification_entity=sea_event["notificationEntity"],
        directive_2009_18=sea_event["directive_2009_18"],
        coastal_state=sea_event["coastalState"],
        lattitude=sea_event["lattitude"],
        longitude=sea_event["longitude"],
        call_sign=sea_event["callSign"],
        flag_state=sea_event["flagState"],
        gross_tonnage=sea_event["grossTonnage"],
        built_year=sea_event["builtYear"],
        hull_material=sea_event["hullMaterial"],
        propulsion_type=sea_event["propulsionType"],
        national_location=sea_event["nationalLocation"],
        registry_number=sea_event["registryNumber"],
        imo=sea_event["IMO"],
        occurrence_sea_area=sea_event["occurrenceSeaArea"],
        ship_type=sea_event["shipType"],
        overall_length=sea_event["overallLength"],
        nb_lives_lost=sea_event["nbLivesLost"],
        nb_injured_people=sea_event["nbInjuredPeople"],
        nb_missing_people=sea_event["nbMissingPeople"],
        processing_status=sea_event["processingStatus"],
    )
