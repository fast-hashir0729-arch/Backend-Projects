from fastapi import HTTPException

from app import repository


def get_tasks(search=None, done=None):
    return repository.get_tasks(search, done)


def get_task(id: int):
    return repository.get_task(id)


def create_task(title: str):
    if not title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    return repository.create_task(title)


def update_task(id: int, title: str, done: bool):
    return repository.update_task(id, title, done)


def delete_task(id: int):
    return repository.delete_task(id)