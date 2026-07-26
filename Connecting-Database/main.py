from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
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


@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    allTasks = cursor.fetchall()
    tasks = []
    for row in allTasks:
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