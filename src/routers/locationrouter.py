from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from src.dependency import get_db, oath2_scheme
from src.models.location import Location
from src.models.user import User
from src.services.auth import authservice
from src.services import locationservice
from src.schemas.location import GetLocation, CreateLocation

router = APIRouter()

@router.get("/locations")
def get_locations(token: str = Depends(oath2_scheme), db: Session = Depends(get_db)) -> list[GetLocation]:
    user:User = authservice.validate_token(token, db)
    if user:
        location_obj: list[Location] = locationservice.get_locations(db)
        locations: list[GetLocation] = [GetLocation(
            id=l.id,
            name=l.name,
            building=l.building,
            floor=l.floor,
            created_at=l.created_at,
            updated_at=l.updated_at
        ) for l in location_obj]

        return locations

@router.post("/location")
def create_location(token: str = Depends(oath2_scheme), data: CreateLocation = Body(...), db: Session = Depends(get_db)) -> GetLocation:
    user: User = authservice.validate_token(token, db)
    if user:
        location_obj: Location = locationservice.create_location(user.id, data.name, data.building, data.floor, db)

        return GetLocation(
            id=location_obj.id,
            name=location_obj.name,
            building=location_obj.building,
            floor=location_obj.floor,
            created_at=location_obj.created_at,
            updated_at=location_obj.updated_at
        )
        