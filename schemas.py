from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
