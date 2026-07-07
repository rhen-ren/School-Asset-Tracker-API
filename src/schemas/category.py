from pydantic import BaseModel
from datetime import datetime

class GetCategory(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

class GetAllCategory(BaseModel):
    categories: list[GetCategory]

class CreateCategory(BaseModel):
    name: str
    description: str
