from typing import Optional

from config import ENVIRONMENT
from src.entities import SeaEvent
from src.io.demo_data import demo_sea_events


class SeaEventRepository:
    _sea_events: list[dict] = []

    def get_all(self) -> list[SeaEvent]:
        return [
            SeaEventRepository.sea_event_dict_to_entity(sea_event)
            for sea_event in self._sea_events
        ]

    def get_by_uuid(self, uuid: str) -> Optional[SeaEvent]:
        for sea_event in self._sea_events:
            if sea_event["uuid"] == uuid:
                return SeaEventRepository.sea_event_dict_to_entity(sea_event)

        return None

    @staticmethod
    def sea_event_dict_to_entity(sea_event_dict: dict) -> SeaEvent:
        return SeaEvent(
            uuid=sea_event_dict["uuid"],
            ship_name=sea_event_dict["shipName"],
            event_type=sea_event_dict["eventType"],
            occurrence_date=sea_event_dict["occurrenceDate"],
            occurrence_time=sea_event_dict["occurrenceTime"],
            occurrence_national_id=sea_event_dict["occurrenceNationalId"],
            notification_date=sea_event_dict["notificationDate"],
            notification_time=sea_event_dict["notificationTime"],
            notification_entity=sea_event_dict["notificationEntity"],
            directive_2009_18=sea_event_dict["directive_2009_18"],
            coastal_state=sea_event_dict["coastalState"],
            lattitude=sea_event_dict["lattitude"],
            longitude=sea_event_dict["longitude"],
            call_sign=sea_event_dict["callSign"],
            flag_state=sea_event_dict["flagState"],
            gross_tonnage=sea_event_dict["grossTonnage"],
            built_year=sea_event_dict["builtYear"],
            hull_material=sea_event_dict["hullMaterial"],
            propulsion_type=sea_event_dict["propulsionType"],
            national_location=sea_event_dict["nationalLocation"],
            registry_number=sea_event_dict["registryNumber"],
            imo=sea_event_dict["IMO"],
            occurrence_sea_area=sea_event_dict["occurrenceSeaArea"],
            ship_type=sea_event_dict["shipType"],
            overall_length=sea_event_dict["overallLength"],
            nb_lives_lost=sea_event_dict["nbLivesLost"],
            nb_injured_people=sea_event_dict["nbInjuredPeople"],
            nb_missing_people=sea_event_dict["nbMissingPeople"],
        )


sea_events_repository = SeaEventRepository()
if ENVIRONMENT == "demo":
    sea_events_repository._sea_events = demo_sea_events.copy()
