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
            label=sea_event["label"],
            type=sea_event["type"],
            date=sea_event["date"],
            time=sea_event["time"],
            cross_entity=sea_event["crossEntity"],
            sitrep_number=sea_event["sitrepNumber"],
            region=sea_event["region"],
            ship_type=sea_event["shipType"],
            imo_number=sea_event["imoNumber"],
            immat_number=sea_event["immatNumber"],
            lht=sea_event["lht"],
            casualty_number=sea_event["casualtyNumber"],
            missing_number=sea_event["missingNumber"],
            injured_number=sea_event["injuredNumber"],
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
