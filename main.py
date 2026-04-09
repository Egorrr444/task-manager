from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    name: str

class TaskCreate(BaseModel):
    name: str


db: list[Task] = []
next_id = 1


@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, name=task.name)
    db.append(new_task)
    next_id += 1
    return new_task




@app.get("/tasks/", response_model=list[Task])
def get_all_tasks():
    return db