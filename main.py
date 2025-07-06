from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from database import Base, engine, SessionLocal
from models import Task
from schemas import TaskCreate, TaskUpdate, Task as TaskSchema

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ CORS Middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables in SQLite
Base.metadata.create_all(bind=engine)

# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Optional welcome route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Task Tracker API"}

# ✅ Create Task
@app.post("/tasks", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ✅ Get All Tasks (with optional filtering)
@app.get("/tasks", response_model=List[TaskSchema])
def get_tasks(is_completed: Optional[bool] = None, db: Session = Depends(get_db)):
    if is_completed is None:
        return db.query(Task).all()
    return db.query(Task).filter(Task.is_completed == is_completed).all()

# ✅ Get Task by ID
@app.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ✅ Update Task
@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in updated_task.dict().items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

# ✅ Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted"}