import pytest

from src.io.repositories import sea_events_repository
from src.usecases import get_sea_events


@pytest.mark.parametrize("dataset_name", ["sea-events-1", "sea-events-2"])
def test_get_sea_events(monkeypatch, dataset_sea_events, dataset_name):
    monkeypatch.setattr(
        sea_events_repository, "get_all", lambda: dataset_sea_events[dataset_name]
    )
    expected_sea_events = dataset_sea_events[dataset_name]

    all_sea_events = get_sea_events()

    assert expected_sea_events == all_sea_events
