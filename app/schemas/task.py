from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    description: str 
    completed: bool

class TaskCreate(BaseModel):
    name: str
    description: str