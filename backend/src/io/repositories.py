from typing import Optional

from config import ENVIRONMENT
from src.entities import SeaEvent
from src.io.demo_data import demo_sea_events


class SeaEventRepository:
    _sea_events: list[dict] = []

    def get_all(self) -> list[SeaEvent]:
        return [
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
            for sea_event in self._sea_events
        ]

    def get_by_uuid(self, uuid: str) -> Optional[SeaEvent]:
        for sea_event in self._sea_events:
            if sea_event["uuid"] == uuid:
                return SeaEvent(
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

        return None


sea_events_repository = SeaEventRepository()
if ENVIRONMENT == "demo":
    sea_events_repository._sea_events = demo_sea_events.copy()
