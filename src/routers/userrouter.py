from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependency import get_db

router = APIRouter()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    pass

@router.post("/user")
async def create_user(db: Session = Depends(get_db)):
    pass

@router.get("/user")
async def get_user(db: Session = Depends(get_db)):
    pass

@router.get("/user/login")
async def login_user(db: Session = Depends(get_db)):
    pass