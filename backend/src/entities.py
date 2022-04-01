from pydantic import BaseModel


class SeaEvent(BaseModel):

    uuid: str
    ship_name: str
    event_type: str
    occurrence_date: str
    occurrence_time: str
    occurrence_national_id: str
    notification_date: str
    notification_time: str
    notification_entity: str
    directive_2009_18: str
    coastal_state: str
    lattitude: str
    longitude: str
    call_sign: str
    flag_state: str
    gross_tonnage: str
    built_year: str
    hull_material: str
    propulsion_type: str
    national_location: str
    registry_number: str
    imo: str
    occurrence_sea_area: str
    ship_type: str
    overall_length: str
    nb_lives_lost: str
    nb_injured_people: str
    nb_missing_people: str
    processing_status: str
