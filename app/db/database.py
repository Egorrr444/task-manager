from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False}, echo=True)

Base = declarative_base()


# создаем класс сессии
SessionLocal = sessionmaker(autoflush=False, bind=engine)

