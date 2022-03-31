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


sea_events_repository = SeaEventRepository()
if ENVIRONMENT == "demo":
    sea_events_repository._sea_events = demo_sea_events.copy()
