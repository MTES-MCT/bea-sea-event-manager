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
                ship_name=sea_event["shipName"],
                event_type=sea_event["eventType"],
                occurrence_date=sea_event["occurrenceDate"],
                occurrence_time=sea_event["occurrenceTime"],
                occurrence_national_id=sea_event["occurrenceNationalId"],
                notification_entity=sea_event["notificationEntity"],
                registry_number=sea_event["registryNumber"],
                imo=sea_event["IMO"],
                occurrence_sea_area=sea_event["occurrenceSeaArea"],
                ship_type=sea_event["shipType"],
                overall_length=sea_event["overallLength"],
                nb_lives_lost=sea_event["nbLivesLost"],
                nb_injured_people=sea_event["nbInjuredPeople"],
                nb_missing_people=sea_event["nbMissingPeople"],
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
