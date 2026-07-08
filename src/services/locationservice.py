from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.location import Location
from fastapi.exceptions import HTTPException

#handle getting of all locations
def get_locations(db: Session) -> list[Location]:
    locations: list[Location] = db.execute(select(Location)).scalars().all()
    return locations

#handle creation of location
def create_location(user_id: int, name: str, building: str, floor: str, db: Session) -> Location:
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

#handle update of location
def update_location(user_id: int, location_id: int, name: str, building: str, floor: str, db: Session) -> Location:
    try:
        current_location = db.get(Location, location_id)
        
        if not current_location:
            raise HTTPException(status_code=404)
        
        if current_location.user_id == user_id:
            current_location.name = name
            current_location.building = building
            current_location.floor = floor

            db.commit()
            db.refresh(current_location)
            
            return current_location
        else:
            raise HTTPException(status_code=401)
    except:
        raise HTTPException(status_code=400)