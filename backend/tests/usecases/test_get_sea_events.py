import pytest

from src.io.repositories import sea_events_repository
from src.usecases import get_sea_events, get_sea_event_by_uuid
from src.exceptions import SeaEventNotFoundError


@pytest.mark.parametrize("dataset_name", ["sea-events-1", "sea-events-2"])
def test_get_sea_events(monkeypatch, dataset_sea_events, dataset_name):
    monkeypatch.setattr(
        sea_events_repository, "get_all", lambda: dataset_sea_events[dataset_name]
    )
    expected_sea_events = dataset_sea_events[dataset_name]

    all_sea_events = get_sea_events()

    assert expected_sea_events == all_sea_events


@pytest.mark.parametrize("index", [0, 1])
def test_get_sea_event_by_uuid(monkeypatch, dataset_sea_events, index):
    sea_event_from_repository = dataset_sea_events["sea-events-1"][index]
    monkeypatch.setattr(
        sea_events_repository, "get_by_uuid", lambda uuid: sea_event_from_repository
    )

    expected_sea_event = sea_event_from_repository

    retrieved_sea_event = get_sea_event_by_uuid(uuid=sea_event_from_repository.uuid)

    assert expected_sea_event == retrieved_sea_event


def test_get_sea_event_by_uuid_missing(monkeypatch):
    monkeypatch.setattr(
        sea_events_repository,
        "get_by_uuid",
        lambda uuid: None,
    )
    missing_uuid = "missing-uuid"

    with pytest.raises(SeaEventNotFoundError) as e:
        get_sea_event_by_uuid(uuid=missing_uuid)

    assert missing_uuid in e.value.args[0]
