from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
import enum
from sqlalchemy import String, Enum
from db import Base

class Role(enum.Enum):
    ADMIN = "Admin"
    USER = "User"

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.USER)

    categories: Mapped[list["Category"]] = relationship("Category", back_populates="user")
    assets: Mapped[list["Asset"]] = relationship("Asset", back_populates="user")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="user")
    locations: Mapped[list["Location"]] = relationship("Location", back_populates="user")


