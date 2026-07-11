import shutil
from src.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import File, UploadFile

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#saving img to backend
def save_img(img: UploadFile = File(None)) -> str:
    location: str = f"uploads/{img.filename}"
    with open(location, "wb") as f:
        shutil.copyfileobj(img.file, f)

    return location


oauth2_scheme = OAuth2PasswordBearer("/user/login")