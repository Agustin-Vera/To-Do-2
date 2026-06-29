from sqlalchemy.orm import Session
from app.repositories.task_repository import get_all_tasks, create_task, get_unique_task
from app.schemas.task import TaskCreate


def list_tasks(db: Session):
    return get_all_tasks(db)


def get_task(db: Session, id: int):
    
    return get_unique_task(db, int)


def create_new_task(db: Session, task: TaskCreate):
    return create_task(db, task)