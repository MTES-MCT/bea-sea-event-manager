from pydantic import BaseModel


class SeaEvent(BaseModel):

    uuid: str
    ship_name: str
    event_type: str
    occurrence_date: str
    occurrence_time: str
    occurrence_national_id: str
    notification_entity: str
    registry_number: str
    imo: str
    occurrence_sea_area: str
    ship_type: str
    overall_length: str
    nb_lives_lost: str
    nb_injured_people: str
    nb_missing_people: str
