from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.dependency import get_db
from src.services import userservice
from src.schemas.user import LoginUser, SignupUser
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

@router.post("/user/login")
async def login_user(user_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Token:
    login_user = LoginUser(email = user_data.username, password = user_data.password)
    return userservice.login_user(login_user.email, login_user.password, db)

@router.post("/user/signup")
async def signup_user(user_data: SignupUser, db: Session = Depends(get_db)) -> Token:
    return userservice.signup_user(
        name = user_data.name,
        email = user_data.email,
        password = user_data.password,
        role = user_data.role,
        db = db
    )