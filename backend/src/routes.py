from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field

from src.usecases import get_sea_events, get_sea_event_by_uuid
from src.exceptions import SeaEventNotFoundError

default_router = APIRouter()


@default_router.get("/", status_code=200)
def live():
    return {"message": "Hello World"}


class ApiSchema(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class SeaEventOutput(ApiSchema):

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
    processing_status: str = Field(..., alias="processingStatus")


@default_router.get("/sea-events", status_code=200, response_model=list[SeaEventOutput])
def retrieve_sea_events():
    all_sea_events = get_sea_events()
    return [SeaEventOutput.from_orm(sea_event) for sea_event in all_sea_events]


class SeaEventOutputDetailed(ApiSchema):
    uuid: str
    ship_name: str = Field(..., alias="shipName")
    event_type: str = Field(..., alias="eventType")
    occurrence_date: str = Field(..., alias="occurrenceDate")
    occurrence_time: str = Field(..., alias="occurrenceTime")
    occurrence_national_id: str = Field(..., alias="occurrenceNationalId")
    notification_date: str = Field(..., alias="notificationDate")
    notification_time: str = Field(..., alias="notificationTime")
    notification_entity: str = Field(..., alias="notificationEntity")
    directive_2009_18: str = Field(..., alias="directive_2009_18")
    coastal_state: str = Field(..., alias="coastalState")
    lattitude: str = Field(..., alias="lattitude")
    longitude: str = Field(..., alias="longitude")
    call_sign: str = Field(..., alias="callSign")
    flag_state: str = Field(..., alias="flagState")
    gross_tonnage: str = Field(..., alias="grossTonnage")
    built_year: str = Field(..., alias="builtYear")
    hull_material: str = Field(..., alias="hullMaterial")
    propulsion_type: str = Field(..., alias="propulsionType")
    national_location: str = Field(..., alias="nationalLocation")
    registry_number: str = Field(..., alias="registryNumber")
    imo: str = Field(..., alias="IMO")
    occurrence_sea_area: str = Field(..., alias="occurrenceSeaArea")
    ship_type: str = Field(..., alias="shipType")
    overall_length: str = Field(..., alias="overallLength")
    nb_lives_lost: str = Field(..., alias="nbLivesLost")
    nb_missing_people: str = Field(..., alias="nbMissingPeople")
    nb_injured_people: str = Field(..., alias="nbInjuredPeople")
    processing_status: str = Field(..., alias="processingStatus")


@default_router.get(
    "/sea-events/{uuid}", status_code=200, response_model=SeaEventOutputDetailed
)
def retrieve_sea_event_by_uuid(uuid: str):
    try:
        sea_event = get_sea_event_by_uuid(uuid=uuid)
    except SeaEventNotFoundError:
        raise HTTPException(status_code=404, detail="Sea event not found")

    return SeaEventOutputDetailed.from_orm(sea_event)
