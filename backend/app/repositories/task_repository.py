from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate


def get_all_tasks(db: Session):
    return db.query(Task).all()


def get_unique_task(db: Session, id: int):
    task = db.get(Task, id)
    
    #task_find = select(Task).where(Task.id == id) # busqeudas selectivas, podria no ser por id
    
    if not task:
        raise HTTPException(status_code=404, detail="Task no encontrado")

    return task

# Task - modelo de sqlalchemy
def create_task(db: Session, task: TaskCreate):
    new_task = Task(**task.model_dump()) # convierte modelo pydantic en dict python
    try:
        db.add(new_task)     # realizar post
        db.commit()          # confirmando
        db.refresh(new_task) # me traigo lo creado
        return new_task
    except SQLAlchemyError:
        db.rollback()        # deshacer todo
        raise HTTPException(status_code=500, detail="Error al crear tarea")
        
        

def update_task(db: Session, id: int, task=TaskCreate):
    oldTask= db.get(Task, id)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task no encontrado")
    
    updatedTask = task.model_dump(exclude_unset=True)
    
    for key, value in update_task.items():
        setattr(oldTask, key, value)
        
    db.add(oldTask)
    db.commit()
    db.refresh(oldTask)
    
    return oldTask
