from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from src.dependency import get_db, oath2_scheme
from src.schemas.asset import CreateAsset, GetAsset
from src.services.auth import authservice
from src.services import assetservice

router = APIRouter()

@router.get("/assets")
def get_assets(db: Session = Depends(get_db)):
    pass

@router.get("/asset/{asset_id}")
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    pass

@router.post("/asset")
def create_asset(token: str = Depends(oath2_scheme), data: CreateAsset = Body(...), db: Session = Depends(get_db)):
    user = authservice.validate_token(token)
    if user:
        #TODO:
        asset_obj = assetservice.create_asset()

@router.put("/asset/{asset_id}")
def update_asset(asset_id: int, db: Session = Depends(get_db)):
    pass