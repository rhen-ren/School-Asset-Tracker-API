from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from src.dependency import get_db
from src.services import userservice
from src.schemas.user import LoginUser
from src.schemas.auth.token import Token

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
async def login_user(user_data: LoginUser = Body(...), db: Session = Depends(get_db)) -> Token:
    return userservice.login_user(user_data.email, user_data.password)