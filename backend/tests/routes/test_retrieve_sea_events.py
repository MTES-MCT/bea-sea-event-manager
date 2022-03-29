from fastapi.testclient import TestClient
import pytest

from src.main import app
from src import routes


@pytest.mark.parametrize("dataset_name", ["sea-events-1", "sea-events-2"])
def test_retrieve_sea_events(monkeypatch, dataset_sea_events, dataset_name):
    sea_events_to_retrieve = dataset_sea_events[dataset_name]

    monkeypatch.setattr(routes, "get_sea_events", lambda: sea_events_to_retrieve.copy())
    client = TestClient(app)
    expected_response = [
        {
            "uuid": sea_event.uuid,
            "label": sea_event.label,
            "type": sea_event.type,
            "date": sea_event.date,
            "time": sea_event.time,
            "CrossEntity": sea_event.CrossEntity,
            "sitrepNumber": sea_event.sitrepNumber,
            "region": sea_event.region,
            "shipType": sea_event.shipType,
            "imoNumber": sea_event.imoNumber,
            "immatNumber": sea_event.immatNumber,
            "lht": sea_event.lht,
            "casualtyNumber": sea_event.casualtyNumber,
            "missingNumber": sea_event.missingNumber,
            "injuredNumber": sea_event.injuredNumber,
        }
        for sea_event in sea_events_to_retrieve
    ]

    response = client.get("/sea-events")

    assert response.status_code == 200
    assert response.json() == expected_response
