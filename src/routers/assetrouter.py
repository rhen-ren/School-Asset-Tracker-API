from fastapi import APIRouter, Depends, Body, Form, UploadFile, File
from sqlalchemy.orm import Session
from src.dependency import get_db, oauth2_scheme, save_img
from src.models.asset import Asset
from src.models.user import User
from src.schemas.asset import CreateAsset, GetAsset
from src.services.auth import authservice
from src.services import assetservice

router = APIRouter()

@router.get("/assets")
def get_assets(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> list[GetAsset]:
    user = authservice.validate_token(token)
    if user:
        asset_obj: list[Asset] = assetservice.get_assets(db)
        assets: list[GetAsset] = [GetAsset(
            id=a.id, name=a.name, status=a.status, serial_number=a.serial_number, purchase_date= a.purchase_date,
            img_url=a.img_url, created_at=a.created_at, updated_at=a.updated_at
        ) for a in asset_obj]

        return assets

@router.get("/assets/{asset_id}")
def get_asset(asset_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> GetAsset:
    user: User = authservice.validate_token(token)
    if user:
        asset_obj = assetservice.get_asset(asset_id, db)

        return GetAsset(
            id=asset_obj.id,
            name=asset_obj.name,
            status=asset_obj.status,
            serial_number=asset_obj.serial_number,
            purchase_date=asset_obj.purchase_date,
            img_url=asset_obj.img_url,
            created_at=asset_obj.created_at,
            updated_at=asset_obj.updated_at
        )
@router.post("/assets")
def create_asset(token: str = Depends(oauth2_scheme), data: CreateAsset = Form(...), img: str = Depends(save_img), db: Session = Depends(get_db)):
    user: User = authservice.validate_token(token)
    if user:
        asset_obj = assetservice.create_asset(user.id, data.name, data.category_id, data.location_id, data.status, data.serial_number, data.purchase_date, data.img_url, db)

        return GetAsset(
            id=asset_obj.id,
            name=asset_obj.name,
            status=asset_obj.status,
            serial_number=asset_obj.serial_number,
            purchase_date=asset_obj.purchase_date,
            img_url=asset_obj.img_url,
            created_at=asset_obj.created_at,
            updated_at=asset_obj.updated_at
        )

@router.put("/asset/{asset_id}")
def update_asset(asset_id: int, db: Session = Depends(get_db)):
    pass