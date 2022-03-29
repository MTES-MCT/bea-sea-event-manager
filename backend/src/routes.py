from fastapi.routing import APIRouter
from pydantic import BaseModel

from src.usecases import get_sea_events


default_router = APIRouter()


@default_router.get("/", status_code=200)
def live():
    return {"message": "Hello World"}


class SeaEventOutput(BaseModel):
    class Config:
        orm_mode = True

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


@default_router.get("/sea-events", status_code=200, response_model=list[SeaEventOutput])
def retrieve_sea_events():
    all_sea_events = get_sea_events()
    return [SeaEventOutput.from_orm(sea_event) for sea_event in all_sea_events]
