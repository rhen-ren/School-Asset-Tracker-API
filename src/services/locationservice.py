from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.location import Location
from fastapi.exceptions import HTTPException

#handle getting of all locations
def get_locations(db: Session) -> list[Location]:
    locations: list[Location] = db.execute(select(Location)).scalars().all()
    return locations

#TODO: creeate creation of location
def create_location(user_id: int, name: str, building: str, floor: str, db: Session):
    try:
        new_location: Location = Location(
            name=name,
            user_id=user_id,
            building=building,
            floor=floor
        )
        db.add(new_location)
        db.commit()
        db.refresh(new_location)

        return new_location
    except:
        raise HTTPException(status_code=400)