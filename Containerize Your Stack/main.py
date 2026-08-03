from fastapi import FastAPI, HTTPException, status
from typing import Optional
from app.schemas import TaskCreate, TaskUpdate
from app.database import connection, cursor
from app import service

app = FastAPI(title = "Task API", description="A simple CRUD API for managing tasks using FastAPI.", version="1.0.0")


@app.get("/tasks")
def get_tasks(search: Optional[str] = None, done: Optional[bool] = None):
    return service.get_tasks(search, done)


@app.get("/tasks/{id}")
def get_task(id: int):
    return service.get_task(id)


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    return service.create_task(task.title)


@app.put("/tasks/{id}")
def update_task(id: int, updated_task: TaskUpdate):
    return service.update_task(
        id,
        updated_task.title,
        updated_task.done
    )


@app.delete("/tasks/{id}")
def delete_task(id: int):
    return service.delete_task(id)