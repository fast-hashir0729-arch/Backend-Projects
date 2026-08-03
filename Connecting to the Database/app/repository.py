from app.database import connection, cursor
from fastapi import HTTPException


def get_tasks(search=None, done=None):
    if search:
        cursor.execute(
            "SELECT * FROM tasks WHERE title LIKE ?",
            (f"%{search}%",)
        )
    else:
        cursor.execute("SELECT * FROM tasks")

    data = cursor.fetchall()

    tasks = []

    for row in data:
        task = dict(row)
        task["done"] = bool(task["done"])
        tasks.append(task)

    return tasks




def get_task(id: int):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    task = dict(row)
    task["done"] = bool(task["done"])

    return task


def create_task(title: str):
    cursor.execute(
        "INSERT INTO tasks(title, done) VALUES(?, ?)",
        (title, False)
    )

    connection.commit()

    last_id = cursor.lastrowid

    return {
        "id": last_id,
        "title": title,
        "done": False
    }


def update_task(id: int, title: str, done: bool):
    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, done, id)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    connection.commit()

    return {
        "id": id,
        "title": title,
        "done": done
    }



def delete_task(id: int):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (id,)
    )

    connection.commit()

    task = dict(task)
    task["done"] = bool(task["done"])

    return task