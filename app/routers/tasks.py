from fastapi import APIRouter
from app.schemas.task import Task, TaskCreate
from app.services import task_service

router = APIRouter()


@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    return task_service.create_task(task)

    

@router.get("/tasks/", response_model=list[Task])
def get_all_tasks():
    return task_service.get_all_tasks()