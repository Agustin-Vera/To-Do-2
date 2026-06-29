from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from datetime import datetime

#Esta clase permite modelos ORM como clases para reprentar DB
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    init_date: Mapped[datetime] = mapped_column(Date, nullable=False, default=datetime.utcnow)
    final_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)
    #id_user = Column(Integer, ForeignKey("users.id"), nullable=False)