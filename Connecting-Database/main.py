from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
import sqlite3

app = FastAPI(title = "Task API", description="A simple CRUD API for managing tasks using FastAPI.", version="1.0.0")

connection = sqlite3.connect("tasks.db", check_same_thread=False)

connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

connection.commit()

cursor.execute("SELECT COUNT(*) FROM tasks")

rowCount = cursor.fetchone()[0]

if rowCount == 0:
    cursor.execute('INSERT INTO tasks (title, done) VALUES ("Study FastAPI",False)')
    cursor.execute('INSERT INTO tasks (title, done) VALUES ("Go to the gym",True)')
    cursor.execute('INSERT INTO tasks (title, done) VALUES ("Complete internship assignment",False)')
    connection.commit()


class TaskCreate(BaseModel):
    title: str 

class TaskUpdate(BaseModel):
    title: str
    done: bool

@app.get("/tasks")
def get_tasks(search: Optional[str] = None, done: Optional[bool] = None):

    if search:
        cursor.execute("SELECT * FROM tasks WHERE title LIKE ?", (f"%{search}%",))
    else:
        cursor.execute("SELECT * FROM tasks")

    data = cursor.fetchall()

    tasks = []
    for row in data:
        task = dict(row)
        task["done"] = bool(task["done"])
        tasks.append(task)

    return tasks


@app.get("/tasks/{id}")
def get_task(id: int):
    cursor.execute(f"SELECT * FROM tasks WHERE id = {id}")
    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Task {id} not found"
        )

    task = dict(row)
    task["done"] = bool(task["done"])

    return task;


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    cursor.execute("""INSERT INTO tasks(title,done) VALUES(?,?)""",(task.title, False))

    connection.commit()
    lastID = cursor.lastrowid

    return {
        "id": lastID,
        "title": task.title,
        "done": False
    }


@app.put("/tasks/{id}")
def update_task(id: int, updated_task: TaskUpdate):
    cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?", (updated_task.title, updated_task.done, id))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )
    else:
        connection.commit()
        return {
            "id": id,
            "title": updated_task.title,
            "done": updated_task.done
        }


@app.delete("/tasks/{id}")
def delete_task(id: int):

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    task = cursor.fetchone()

    if task == None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))

    connection.commit()

    return task
