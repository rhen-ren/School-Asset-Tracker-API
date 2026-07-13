from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Asset
from fastapi.exceptions import HTTPException

#handles getting of all assets
def get_assets(db: Session) -> list[Asset]:
    assets = db.execute(select(Asset)).scalars().all()
    return assets

#hanldes getting of an asset
def get_asset(asset_id: int, db: Session) -> Asset:
    asset = db.get(Asset, asset_id)
    if asset:
        return asset
    else:
        raise HTTPException(status_code=404)

#handles creation of asset
def create_asset(
        user_id: int, name:str, category_id: int,
        location_id: int, status: str,
        serial_number: str, purchase_date: datetime,
        img_url: str, db: Session) -> Asset:
    try:
        new_asset = Asset(
            name = name,
            category_id = category_id,
            location_id = location_id,
            user_id = user_id,
            status = status,
            serial_number = serial_number,
            purchase_date = purchase_date,
            img_url = img_url
        )

        db.add(new_asset)
        db.commit()
        db.refresh(new_asset)

        return new_asset

    except:
        raise HTTPException(status_code=400)
    
    

    