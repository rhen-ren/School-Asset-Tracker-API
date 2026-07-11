from src.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer("/user/login")