from fastapi import APIRouter
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services import task_service

router = APIRouter()


@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.get("/tasks/", response_model=list[Task])
def get_all_tasks():
    return task_service.get_all_tasks()


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return task_service.get_task(task_id)
    

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    return task_service.delete_task(task_id)
     
    
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    return task_service.update_task(task_id, task_update) 

@router.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    return task_service.update_task(task_id, task_update)