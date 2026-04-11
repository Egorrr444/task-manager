from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import tasks
from app.models.task import Task  # needed for SQLAlchemy

app = FastAPI()

app.include_router(tasks.router)

Base.metadata.create_all(bind=engine)