from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False,default="")
    