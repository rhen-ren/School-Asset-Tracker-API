from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, func, DateTime
from datetime import datetime
from db import Base

class Location(Base):
    __tablename__ = "Location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Asset.id"))
    building: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    floor: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())

    assets: Mapped[list["Asset"]] = relationship("Asset", back_populates="location")
    user: Mapped["User"] = relationship("User", back_populates="locations")