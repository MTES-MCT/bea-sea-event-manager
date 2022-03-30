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
    label: str
    type: str
    date: str
    time: str
    cross_entity: str = Field(..., alias="crossEntity")
    sitrep_number: str = Field(..., alias="sitrepNumber")
    region: str
    ship_type: str = Field(..., alias="shipType")
    imo_number: str = Field(..., alias="imoNumber")
    immat_number: str = Field(..., alias="immatNumber")
    lht: str
    casualty_number: str = Field(..., alias="casualtyNumber")
    missing_number: str = Field(..., alias="missingNumber")
    injured_number: str = Field(..., alias="injuredNumber")


@default_router.get("/sea-events", status_code=200, response_model=list[SeaEventOutput])
def retrieve_sea_events():
    all_sea_events = get_sea_events()
    return [SeaEventOutput.from_orm(sea_event) for sea_event in all_sea_events]
