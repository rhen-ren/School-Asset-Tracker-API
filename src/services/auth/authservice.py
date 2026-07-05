import os
from dotenv import load_dotenv
import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.user import User
from fastapi.exceptions import HTTPException

#get secret key from env
load_dotenv()
SECRETKEY = os.getenv("SECRETKEY")
ALGORITHM = "HS256"
password_hash = PasswordHash.recommended()

#authenticate user
#used for getting correct user
#user check hashed password on db
def authenticate_user(email: str, password: str, db: Session) -> User:
    user: User = db.execute(select(User).where(User.email == email)).scalars().one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="User Not Found")
    if not password_hash.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user


#access token creation
#uses jwt
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRETKEY, algorithm=ALGORITHM)
    return encoded_jwt


