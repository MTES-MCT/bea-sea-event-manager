from src.io.repositories import sea_events_repository
from src.entities import SeaEvent


def get_sea_events() -> list[SeaEvent]:
    all_sea_events = sea_events_repository.get_all()
    return all_sea_events
