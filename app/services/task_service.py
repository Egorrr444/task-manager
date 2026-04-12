from fastapi import HTTPException
from app.models.task import Task 
from app.schemas.task import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session



def create_task(task: TaskCreate, db: Session):
   
    
        new_task = Task(
        title=task.title,
        description=task.description,
        completed=False
    )  
    
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task



def get_all_tasks(db: Session):
    return db.query(Task).all()
    

def get_task(task_id: int, db: Session):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    
def delete_task(task_id: int, db: Session):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        db.delete(task)
        db.commit()
        return task

def update_task(task_id: int, task_update: TaskCreate, db: Session):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        task.title = task_update.title
        task.description = task_update.description
        task.completed = task_update.completed
        db.commit()
        db.refresh(task)
        return task
    
def patch_task(task_id: int, task_update: TaskUpdate, db: Session):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        if task_update.title is not None:
            task.title = task_update.title
        if task_update.description is not None:
            task.description = task_update.description
        if task_update.completed is not None:
            task.completed = task_update.completed
        db.commit()
        db.refresh(task)
        return task