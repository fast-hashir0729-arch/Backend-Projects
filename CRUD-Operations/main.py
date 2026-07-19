from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title = "Task API", description="A simple CRUD API for managing tasks using FastAPI.", version="1.0.0");


tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Go to the gym",
        "done": True
    },
    {
        "id": 3,
        "title": "Complete internship assignment",
        "done": False
    }
]



@app.get("/",
    summary="API information",
    description="Returns basic information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }



@app.get("/health",
    summary="Health check",
    description="Checks whether the API server is running."
)
def health():
    return {
        "status": "ok"
    }



@app.get("/tasks", 
    summary="Get all tasks", 
    description="Returns the complete list of tasks."
)
def get_tasks():
    return tasks



@app.get("/tasks/{id}",
    summary="Get a task by ID",
    description="Returns a single task using its unique ID."
)
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )



class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        example="Buy milk",
        description="The title of the task."
    )


class TaskUpdate(BaseModel):
    title: str = Field(
        ...,
        example="Buy groceries",
        description="Updated title of the task."
    )

    done: bool = Field(
        ...,
        example=True,
        description="Whether the task has been completed."
    )

@app.post("/tasks", 
    status_code=status.HTTP_201_CREATED,     
    summary="Create a new task",
    description="Creates a new task with a unique ID and marks it as not completed"
)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )
    

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task



@app.put("/tasks/{id}",     
    summary="Update a task",
    description="Updates the title and completion status of an existing task."
)


def update_task(id: int, updated_task: TaskUpdate):

    for task in tasks:

        if task["id"] == id:

            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )


@app.delete("/tasks/{id}", 
    status_code=status.HTTP_204_NO_CONTENT,    
    summary="Delete a task",
    description="Deletes a task using its ID."
)
def delete_task(id: int):

    for index, task in enumerate(tasks):

        if task["id"] == id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )