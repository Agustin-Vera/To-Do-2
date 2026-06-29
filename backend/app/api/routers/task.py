from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import list_tasks, create_new_task

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return list_tasks(db)


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_new_task(db, task)

#@router.get("/db-test")
#def test_db_connection(db: Session = Depends(get_db)):
#    db.execute(text("SELECT 1"))
#    return {"message": "Conexión exitosa"}