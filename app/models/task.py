from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# строка подключения
engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False}, echo=True)


# создаем движок SqlAlchemy
Base = declarative_base()


# создаем класс сессии
SessionLocal = sessionmaker(autoflush=False, bind=engine)


# создаем модель, объекты которой будут храниться в бд
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)