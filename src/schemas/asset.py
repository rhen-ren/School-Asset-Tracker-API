from pydantic import BaseModel
from datetime import datetime

class GetAsset(BaseModel):
    id: int
    name: str
    status: str
    serial_number: int
    purchase_date: datetime
    img_url: str
    created_at: datetime
    updated_at: datetime

class CreateAsset(BaseModel):
    name: str
    status: str
    serial_number: int
    purchase_date: datetime
    img_url: str
    created_at: datetime
    updated_at: datetime
    category: int
    location: int