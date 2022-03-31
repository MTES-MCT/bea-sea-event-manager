from src.io.repositories import sea_events_repository
from src.entities import SeaEvent
from src.exceptions import SeaEventNotFoundError


def get_sea_events() -> list[SeaEvent]:
    all_sea_events = sea_events_repository.get_all()
    return all_sea_events


def get_sea_event_by_uuid(uuid: str) -> SeaEvent:
    sea_event_from_repository = sea_events_repository.get_by_uuid(uuid=uuid)

    if sea_event_from_repository is None:
        raise SeaEventNotFoundError(uuid=uuid)

    return sea_event_from_repository
