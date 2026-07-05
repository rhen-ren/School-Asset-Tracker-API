from sqlalchemy.orm import DeclarativeBase,  Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, func, DateTime
from datetime import datetime
from db import Base

class Category(Base):
    __tablename__ = "Category"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship("User", back_populates="categories")
    assest: Mapped[list["Asset"]] = relationship("Asset", back_populates="category")
    
