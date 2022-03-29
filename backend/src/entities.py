from pydantic import BaseModel


class SeaEvent(BaseModel):

    uuid: str
    label: str
    type: str
    date: str
    time: str
    CrossEntity: str
    sitrepNumber: str
    region: str
    shipType: str
    imoNumber: str
    immatNumber: str
    lht: str
    casualtyNumber: str
    missingNumber: str
    injuredNumber: str
