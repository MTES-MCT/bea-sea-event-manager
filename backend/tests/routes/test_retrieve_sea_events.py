from fastapi.testclient import TestClient
import pytest

from src.main import app
from src import routes
from src.entities import SeaEvent


@pytest.mark.parametrize("dataset_name", ["sea-events-1", "sea-events-2"])
def test_retrieve_sea_events(
    monkeypatch, dataset_sea_events: dict[str, list[SeaEvent]], dataset_name: str
):
    sea_events_to_retrieve = dataset_sea_events[dataset_name]

    monkeypatch.setattr(routes, "get_sea_events", lambda: sea_events_to_retrieve.copy())
    client = TestClient(app)
    expected_response = [
        {
            "uuid": sea_event.uuid,
            "label": sea_event.ship_name,
            "type": sea_event.event_type,
            "date": sea_event.occurrence_date,
            "time": sea_event.occurrence_time,
            "crossEntity": sea_event.notification_entity,
            "sitrepNumber": sea_event.occurrence_national_id,
            "region": sea_event.occurrence_sea_area,
            "shipType": sea_event.ship_type,
            "imoNumber": sea_event.imo,
            "immatNumber": sea_event.registry_number,
            "lht": sea_event.overall_length,
            "casualtyNumber": sea_event.nb_lives_lost,
            "missingNumber": sea_event.nb_missing_people,
            "injuredNumber": sea_event.nb_injured_people,
        }
        for sea_event in sea_events_to_retrieve
    ]

    response = client.get("/sea-events")

    assert response.status_code == 200
    assert response.json() == expected_response
