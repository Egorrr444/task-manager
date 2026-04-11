from app.models.task import Task
from app.models.task import SessionLocal
from app.schemas.task import TaskCreate 



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
    