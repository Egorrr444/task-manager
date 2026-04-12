from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services import task_service

router = APIRouter()


@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db = Depends(get_db)):
    return task_service.create_task(task, db)


@router.get("/tasks/", response_model=list[Task])
def get_all_tasks(db = Depends(get_db)):
    return task_service.get_all_tasks(db)


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db = Depends(get_db)):
    return task_service.get_task(task_id, db)
    

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db = Depends(get_db)):
    return task_service.delete_task(task_id, db)
     
    
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate, db = Depends(get_db)):
    return task_service.update_task(task_id, task_update, db) 


@router.patch("/tasks/{task_id}", response_model=Task)
def patch_task(task_id: int, task_update: TaskUpdate, db = Depends(get_db)):
    return task_service.update_task(task_id, task_update, db)