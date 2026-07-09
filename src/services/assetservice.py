from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Asset

def get_assets(db: Session) -> list[Asset]:
    assets = db.execute(select(Asset)).scalars().all()
    return assets