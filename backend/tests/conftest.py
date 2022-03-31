import pytest

from src.entities import SeaEvent


@pytest.fixture
def dataset_sea_events_as_dict() -> dict[str, list[dict]]:
    return {
        "sea-events-1": [
            {
                "uuid": "acf2178e-6502-4c4f-8117-39a8315be94b",
                "shipName": "ship-name-1",
                "eventType": "event-type-1",
                "occurrenceDate": "2020-01-01",
                "occurrenceTime": "00:00:00",
                "occurrenceNationalId": "occurrence-national-id-1",
                "notificationEntity": "notification-entity-1",
                "registryNumber": "registry-number-1",
                "IMO": "imo-1",
                "occurrenceSeaArea": "occurrence-sea-area-1",
                "shipType": "shipType-1",
                "overallLength": "overall-length-1",
                "nbLivesLost": "lives-lost-1",
                "nbInjuredPeople": "injured-people-1",
                "nbMissingPeople": "missing-people-1",
            },
            {
                "uuid": "acf2178e-6502-4c4f-8117-39a8315be94c",
                "shipName": "ship-name-2",
                "eventType": "event-type-2",
                "occurrenceDate": "2020-01-02",
                "occurrenceTime": "00:00:00",
                "occurrenceNationalId": "occurrence-national-id-2",
                "notificationEntity": "notification-entity-2",
                "registryNumber": "registry-number-2",
                "IMO": "imo-2",
                "occurrenceSeaArea": "occurrence-sea-area-2",
                "shipType": "shipType-2",
                "overallLength": "overall-length-2",
                "nbLivesLost": "lives-lost-2",
                "nbInjuredPeople": "injured-people-2",
                "nbMissingPeople": "missing-people-2",
            },
        ],
        "sea-events-2": [
            {
                "uuid": "acf2178e-6502-4c4f-8117-39a8315be94d",
                "shipName": "ship-name-3",
                "eventType": "event-type-3",
                "occurrenceDate": "2020-01-03",
                "occurrenceTime": "00:00:00",
                "occurrenceNationalId": "occurrence-national-id-3",
                "notificationEntity": "notification-entity-3",
                "registryNumber": "registry-number-3",
                "IMO": "imo-3",
                "occurrenceSeaArea": "occurrence-sea-area-3",
                "shipType": "shipType-3",
                "overallLength": "overall-length-3",
                "nbLivesLost": "lives-lost-3",
                "nbInjuredPeople": "injured-people-3",
                "nbMissingPeople": "missing-people-3",
            },
            {
                "uuid": "acf2178e-6502-4c4f-8117-39a8315be94e",
                "shipName": "ship-name-4",
                "eventType": "event-type-4",
                "occurrenceDate": "2020-01-04",
                "occurrenceTime": "00:00:00",
                "occurrenceNationalId": "occurrence-national-id-4",
                "notificationEntity": "notification-entity-4",
                "registryNumber": "registry-number-4",
                "IMO": "imo-4",
                "occurrenceSeaArea": "occurrence-sea-area-4",
                "shipType": "shipType-4",
                "overallLength": "overall-length-4",
                "nbLivesLost": "lives-lost-4",
                "nbInjuredPeople": "injured-people-4",
                "nbMissingPeople": "missing-people-4",
            },
        ],
    }


@pytest.fixture
def dataset_sea_events(
    dataset_sea_events_as_dict: dict[str, list[dict]]
) -> dict[str, list[SeaEvent]]:
    dataset_sea_events_return = {}
    for dataset_name in dataset_sea_events_as_dict:
        dataset_sea_events_return[dataset_name] = [
            SeaEvent(
                uuid=sea_event_dict["uuid"],
                ship_name=sea_event_dict["shipName"],
                event_type=sea_event_dict["eventType"],
                occurrence_date=sea_event_dict["occurrenceDate"],
                occurrence_time=sea_event_dict["occurrenceTime"],
                occurrence_national_id=sea_event_dict["occurrenceNationalId"],
                notification_entity=sea_event_dict["notificationEntity"],
                registry_number=sea_event_dict["registryNumber"],
                imo=sea_event_dict["IMO"],
                occurrence_sea_area=sea_event_dict["occurrenceSeaArea"],
                ship_type=sea_event_dict["shipType"],
                overall_length=sea_event_dict["overallLength"],
                nb_lives_lost=sea_event_dict["nbLivesLost"],
                nb_injured_people=sea_event_dict["nbInjuredPeople"],
                nb_missing_people=sea_event_dict["nbMissingPeople"],
            )
            for sea_event_dict in dataset_sea_events_as_dict[dataset_name]
        ]
    return dataset_sea_events_return
