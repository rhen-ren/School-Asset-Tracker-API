from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from src.dependency import get_db, oath2_scheme
from src.models.user import User
from src.models.category import Category
from src.schemas.category import GetCategory, CreateCategory
from src.services.auth import authservice
from src.services import categoryservice

router = APIRouter()

@router.get("/categories")
def get_categories(token: str = Depends(oath2_scheme),db: Session = Depends(get_db)) -> list[GetCategory]:
    user: User = authservice.validate_token(token, db)
    if user:
        categories_obj: list[Category] = categoryservice.get_categories(db)
        categorires: list[GetCategory] = [GetCategory(id=c.id, name=c.name, description=c.description, created_at=c.created_at, updated_at=c.updated_at) for c in categories_obj]
        return categorires
    
@router.post("/category")
def create_category(token: str = Depends(oath2_scheme), data: CreateCategory = Body(...), db: Session = Depends(get_db)) -> GetCategory:
    user: User = authservice.validate_token(token, db)
    if user:
        category_obj: Category = categoryservice.create_category(user.id, data.name, data.description, db)
        return GetCategory(
            id=category_obj.id,
            name=category_obj.name,
            description=category_obj.description,
            created_at=category_obj.created_at,
           updated_at=category_obj.updated_at 
        )

@router.put("/category/{category_id}")
def update_category(token: str = Depends(oath2_scheme), category_id: int = None, data: CreateCategory = Body(...), db: Session = Depends(get_db)):
    user: User = authservice.validate_token(token, db)
    if user:
        category_obj: Category = categoryservice.update_category(category_id, user.id, data.name, data.description, db)
        return GetCategory(
            id=category_obj.id,
            name=category_obj.name,
            description=category_obj.description,
            created_at=category_obj.created_at,
           updated_at=category_obj.updated_at 
        )