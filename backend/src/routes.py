from fastapi.routing import APIRouter
from pydantic import BaseModel, Field

from src.usecases import get_sea_events


default_router = APIRouter()


@default_router.get("/", status_code=200)
def live():
    return {"message": "Hello World"}


class SeaEventOutput(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    uuid: str
    ship_name: str = Field(..., alias="label")
    event_type: str = Field(..., alias="type")
    occurrence_date: str = Field(..., alias="date")
    occurrence_time: str = Field(..., alias="time")
    notification_entity: str = Field(..., alias="crossEntity")
    occurrence_national_id: str = Field(..., alias="sitrepNumber")
    registry_number: str = Field(..., alias="immatNumber")
    imo: str = Field(..., alias="imoNumber")
    occurrence_sea_area: str = Field(..., alias="region")
    ship_type: str = Field(..., alias="shipType")
    overall_length: str = Field(..., alias="lht")
    nb_lives_lost: str = Field(..., alias="casualtyNumber")
    nb_missing_people: str = Field(..., alias="missingNumber")
    nb_injured_people: str = Field(..., alias="injuredNumber")


@default_router.get("/sea-events", status_code=200, response_model=list[SeaEventOutput])
def retrieve_sea_events():
    all_sea_events = get_sea_events()
    return [SeaEventOutput.from_orm(sea_event) for sea_event in all_sea_events]
