from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Asset
from fastapi.exceptions import HTTPException

def get_assets(db: Session) -> list[Asset]:
    assets = db.execute(select(Asset)).scalars().all()
    return assets

def get_asset(asset_id: int, db: Session) -> Asset:
    asset = db.get(Asset, asset_id)
    if asset:
        return asset
    else:
        raise HTTPException(status_code=404)
    