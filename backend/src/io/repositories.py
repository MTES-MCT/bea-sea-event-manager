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
                CrossEntity=sea_event["CrossEntity"],
                sitrepNumber=sea_event["sitrepNumber"],
                region=sea_event["region"],
                shipType=sea_event["shipType"],
                imoNumber=sea_event["imoNumber"],
                immatNumber=sea_event["immatNumber"],
                lht=sea_event["lht"],
                casualtyNumber=sea_event["casualtyNumber"],
                missingNumber=sea_event["missingNumber"],
                injuredNumber=sea_event["injuredNumber"],
            )
            for sea_event in self._sea_events
        ]


sea_events_repository = SeaEventRepository()
if ENVIRONMENT == "demo":
    sea_events_repository._sea_events = demo_sea_events.copy()
