# schemas/task.py
from datetime import date
from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    name: str
    description: str
    state: str
    init_date: date
    final_date: date
    id_user: int
    
    # model_config - podria recibir/validar objetos

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    state: str
    init_date: date
    final_date: date
    id_user: int