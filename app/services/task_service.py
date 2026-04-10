from app.schemas.task import Task, TaskCreate


db: list[Task] = []
next_id = 1



def create_task(task: TaskCreate):
    global next_id

    new_task = Task(
        id=next_id,
        name=task.name,
        description=task.description,
        completed=False
    )

    db.append(new_task)
    next_id += 1
    return new_task



def get_all_tasks():
    return db
