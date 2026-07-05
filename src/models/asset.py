from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, func, ForeignKey, Enum, DateTime
import enum
from db import Base
from datetime import datetime

class Status(enum.Enum):
    AVAILABLE = "Available"
    ASSIGNED = "Assigned"
    LOST = "Lost"
    INREPAIR = "In-Repair"

class Asset(Base):
    __tablename__ = "Asset"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("Category.id"))
    location_id: Mapped[int] = mapped_column(ForeignKey("Location.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    status: Mapped[Status] = mapped_column(Enum(Status))
    serial_number: Mapped[str] = mapped_column(String(300), nullable=False)
    purchase_date: Mapped[datetime] = mapped_column(DateTime())
    img_url: Mapped[str] = mapped_column(String(200), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now(), onupdate=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now(), onupdate=func.now())

    category: Mapped["Category"] = relationship("Category", back_populates="assets")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="asset")
    user: Mapped["User"] = relationship("User", back_populates="assets")
    location: Mapped["Location"] = relationship("Location", back_populates="assets")