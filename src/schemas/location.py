from pydantic import BaseModel
from datetime import datetime

class GetLocation(BaseModel):
    id: int
    name: str
    building: str
    floor: str
    created_at: datetime
    updated_at: datetime

class CreateLocation(BaseModel):
    name: str
    building: str
    floor: str