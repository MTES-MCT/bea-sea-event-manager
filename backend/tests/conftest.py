import pytest


from src.entities import SeaEvent


@pytest.fixture
def dataset_sea_events_as_dict() -> dict[str, list[dict]]:
    return {
        "sea-events-1": [
            {
                "uuid": "acf2178e-6502-4c4f-8117-39a8315be94b",
                "label": "label-1",
                "type": "type-1",
                "date": "date-1",
                "time": "time-1",
                "crossEntity": "crossEntity-1",
                "sitrepNumber": "sitrepNumber-1",
                "region": "region-1",
                "shipType": "shipType-1",
                "imoNumber": "imoNumber-1",
                "immatNumber": "immatNumber-1",
                "lht": "lht-1",
                "casualtyNumber": "casualtyNumber-1",
                "missingNumber": "missingNumber-1",
                "injuredNumber": "injuredNumber-1",
            },
            {
                "uuid": "69f8b2e0-aca4-404b-9342-f69e5013545f",
                "label": "label-2",
                "type": "type-2",
                "date": "date-2",
                "time": "time-2",
                "crossEntity": "crossEntity-2",
                "sitrepNumber": "sitrepNumber-2",
                "region": "region-2",
                "shipType": "shipType-2",
                "imoNumber": "imoNumber-2",
                "immatNumber": "immatNumber-2",
                "lht": "lht-2",
                "casualtyNumber": "casualtyNumber-2",
                "missingNumber": "missingNumber-2",
                "injuredNumber": "injuredNumber-2",
            },
        ],
        "sea-events-2": [
            {
                "uuid": "9a1e72b5-7c15-4517-a9b9-377495d6612f",
                "label": "label-3",
                "type": "type-3",
                "date": "date-3",
                "time": "time-3",
                "crossEntity": "crossEntity-3",
                "sitrepNumber": "sitrepNumber-3",
                "region": "region-3",
                "shipType": "shipType-3",
                "imoNumber": "imoNumber-3",
                "immatNumber": "immatNumber-3",
                "lht": "lht-3",
                "casualtyNumber": "casualtyNumber-3",
                "missingNumber": "missingNumber-3",
                "injuredNumber": "injuredNumber-3",
            },
            {
                "uuid": "e9f8b2e0-aca4-404b-9342-f69e5013545f",
                "label": "label-4",
                "type": "type-4",
                "date": "date-4",
                "time": "time-4",
                "crossEntity": "crossEntity-4",
                "sitrepNumber": "sitrepNumber-4",
                "region": "region-4",
                "shipType": "shipType-4",
                "imoNumber": "imoNumber-4",
                "immatNumber": "immatNumber-4",
                "lht": "lht-4",
                "casualtyNumber": "casualtyNumber-4",
                "missingNumber": "missingNumber-4",
                "injuredNumber": "injuredNumber-4",
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
                label=sea_event_dict["label"],
                type=sea_event_dict["type"],
                date=sea_event_dict["date"],
                time=sea_event_dict["time"],
                cross_entity=sea_event_dict["crossEntity"],
                sitrep_number=sea_event_dict["sitrepNumber"],
                region=sea_event_dict["region"],
                ship_type=sea_event_dict["shipType"],
                imo_number=sea_event_dict["imoNumber"],
                immat_number=sea_event_dict["immatNumber"],
                lht=sea_event_dict["lht"],
                casualty_number=sea_event_dict["casualtyNumber"],
                missing_number=sea_event_dict["missingNumber"],
                injured_number=sea_event_dict["injuredNumber"],
            )
            for sea_event_dict in dataset_sea_events_as_dict[dataset_name]
        ]
    return dataset_sea_events_return
