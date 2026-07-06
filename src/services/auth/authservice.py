import os
from dotenv import load_dotenv
import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.user import User
from fastapi.exceptions import HTTPException
from src.schemas.auth.token import TokenData, Token

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

#hash a users password
#used when signingup a user
def hash_password(password: str):
    if password:
        return password_hash.hash(password)

#access token creation
#uses jwt
def create_access_token(data: dict) -> Token:
    to_encode: dict = data.copy()
    encoded_jwt: str = jwt.encode(to_encode, SECRETKEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")

#token validation
#returns user account
def validate_token(token: str, db: Session) -> User:
    try:
        payload: dict = jwt.decode(token, SECRETKEY, algorithms=[ALGORITHM])
        email: str | None  = payload.get("email")
        if email is None:
            return None
        token_data = TokenData(email=email)
        user = db.execute(select(User).where(User.email == token_data.email)).scalars().one_or_none()
        if not user:
            raise HTTPException(status_code=401)
        return user
    except Exception as e:
        raise e



