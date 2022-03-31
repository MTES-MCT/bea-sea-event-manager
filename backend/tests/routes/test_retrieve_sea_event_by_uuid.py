from fastapi.testclient import TestClient

from src.main import app
from src import routes
from src.exceptions import SeaEventNotFoundError
from src.entities import SeaEvent


def test_retrieve_sea_event_by_uuid(
    monkeypatch, dataset_sea_events: dict[str, list[SeaEvent]]
):
    sea_event_to_retrieve = dataset_sea_events["sea-events-1"][0]
    monkeypatch.setattr(
        routes,
        "get_sea_event_by_uuid",
        lambda uuid: sea_event_to_retrieve.copy(),
    )
    client = TestClient(app)
    expected_response = {
        "uuid": sea_event_to_retrieve.uuid,
        "occurrenceDate": sea_event_to_retrieve.occurrence_date,
        "occurrenceTime": sea_event_to_retrieve.occurrence_time,
        "eventType": sea_event_to_retrieve.event_type,
        "notificationDate": sea_event_to_retrieve.notification_date,
        "notificationTime": sea_event_to_retrieve.notification_time,
        "notificationEntity": sea_event_to_retrieve.notification_entity,
        "directive2009_18": sea_event_to_retrieve.directive_2009_18,
        "coastalState": sea_event_to_retrieve.coastal_state,
        "lattitude": sea_event_to_retrieve.lattitude,
        "longitude": sea_event_to_retrieve.longitude,
        "occurrenceSeaArea": sea_event_to_retrieve.sea_area,
        "shipName": sea_event_to_retrieve.label,
        "IMO": sea_event_to_retrieve.imo,
        "callSign": sea_event_to_retrieve.call_sign,
        "flagState": sea_event_to_retrieve.coastal_state,
        "registryNumber": sea_event_to_retrieve.registry_number,
        "grossTonnage": sea_event_to_retrieve.gross_tonnage,
        "builtYear": sea_event_to_retrieve.built_year,
        "overallLength": sea_event_to_retrieve.overall_length,
        "hullMaterial": sea_event_to_retrieve.hull_material,
        "propulsionType": sea_event_to_retrieve.propulsion_type,
        "shipType": sea_event_to_retrieve.ship_type,
        "nationalLocation": sea_event_to_retrieve.national_location,
    }

    response = client.get("/sea-events/{uuid}")

    assert response.status_code == 200
    assert response.json() == expected_response


def test_retrieve_sea_event_by_uuid_missing(monkeypatch, dataset_sea_events):
    def mock_get_sea_event_by_uuid(uuid):
        raise SeaEventNotFoundError(uuid)

    monkeypatch.setattr(
        routes,
        "get_sea_event_by_uuid",
        mock_get_sea_event_by_uuid,
    )
    client = TestClient(app)

    response = client.get("/sea-events/{uuid}")

    assert response.status_code == 404
