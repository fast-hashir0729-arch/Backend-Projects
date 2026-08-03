from app.database import connection, cursor
from fastapi import HTTPException


def get_tasks(search=None, done=None):
    if search:
        cursor.execute(
            "SELECT * FROM tasks WHERE title ILIKE %s",
            (f"%{search}%",)
        )
    else:
        cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": row[2]
        })

    return tasks



def get_task(id: int):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }


def create_task(title: str):
    cursor.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (title, False)
    )

    last_id = cursor.fetchone()[0]

    connection.commit()

    return {
        "id": last_id,
        "title": title,
        "done": False
    }


def update_task(id: int, title: str, done: bool):
    cursor.execute(
        """
        UPDATE tasks
        SET title = %s, done = %s
        WHERE id = %s
        RETURNING id;
        """,
        (title, done, id)
    )

    updated = cursor.fetchone()

    if updated is None:
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
        """
        DELETE FROM tasks
        WHERE id = %s
        RETURNING id, title, done;
        """,
        (id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    connection.commit()

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }