from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependency import get_db

router = APIRouter()

@router.get("/assets")
def get_assets(db: Session = Depends(get_db)):
    pass

@router.post("/asset")
def create_asset(db: Session = Depends(get_db)):
    pass

@router.put("/asset/{asset_id}")
def update_asset(asset_id: int, db: Session = Depends(get_db)):
    pass