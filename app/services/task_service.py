from fastapi import HTTPException
from app.models.task import Task 
from app.db.database import SessionLocal
from app.schemas.task import TaskCreate, TaskUpdate



def create_task(task: TaskCreate):
   
    with SessionLocal() as session:
        new_task = Task(
        title=task.title,
        description=task.description,
        completed=False
    )  
    
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task



def get_all_tasks():
    with SessionLocal() as session:
        return session.query(Task).all()
    

def get_task(task_id: int):
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    
def delete_task(task_id: int):
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return task

def update_task(task_id: int, task_update: TaskUpdate):
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        task.title = task_update.title
        task.description = task_update.description
        task.completed = task_update.completed
        session.commit()
        session.refresh(task)
        return task
    
def update_task(task_id: int, task_update: TaskUpdate):
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        if task_update.title is not None:
            task.title = task_update.title
        if task_update.description is not None:
            task.description = task_update.description
        if task_update.completed is not None:
            task.completed = task_update.completed
        session.commit()
        session.refresh(task)
        return task