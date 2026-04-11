from sqlalchemy import Boolean, Column, Integer, String
from app.db.database import Base


# создаем модель, объекты которой будут храниться в бд
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

