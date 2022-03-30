from pydantic import BaseModel


class SeaEvent(BaseModel):

    uuid: str
    label: str
    type: str
    date: str
    time: str
    cross_entity: str
    sitrep_number: str
    region: str
    ship_type: str
    imo_number: str
    immat_number: str
    lht: str
    casualty_number: str
    missing_number: str
    injured_number: str
