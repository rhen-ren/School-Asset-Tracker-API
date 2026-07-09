from pydantic import BaseModel
from datetime import datetime

class GetAsset(BaseModel):
    name: str
    status: str
    serial_number: int
    purchase_date: datetime
    img_url: str
    created_at: datetime
    updated_at: datetime