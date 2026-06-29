from fastapi import FastAPI
from app.api.routers.task import router as task_router

app = FastAPI()

app.include_router(task_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}

