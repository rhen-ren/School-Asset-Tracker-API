from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, func, ForeignKey, Enum, DateTime
import enum
from db import Base
from datetime import datetime

class ActionType(enum.Enum):
    CREATE = "Create"
    UPDATE = "Update"
    CANCEL = "Cancel"
    COMPLETE = "Complete"
    ASSIGN = "Assign"

class Transaction(Base):
    __tablename__ = "Transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    action_type: Mapped[ActionType] = mapped_column(Enum(ActionType), default=ActionType.CREATE)
    notes: Mapped[String] = mapped_column(String(500), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())

    asset: Mapped["Asset"] = relationship("Asset", back_populates="transactions")
    user: Mapped["User"] = relationship("User", back_populates="transactions")

