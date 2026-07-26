# Week 3 - Assignment 1: Task API with SQLite

## Overview

This project is a RESTful CRUD API built using **FastAPI** and **SQLite**.

It is an extension of the previous assignment where tasks were stored in an in-memory Python list. In this assignment, the storage layer has been replaced with a SQLite database, allowing data to persist even after restarting the server.

The API remains exactly the same while only the storage implementation changes.

---

## Features

- Create a new task
- Get all tasks
- Get a task by ID
- Update an existing task
- Delete a task
- Automatic database creation
- Automatic table creation
- Automatic insertion of sample tasks on first run
- Persistent data storage using SQLite

---

## Technologies Used

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Why SQLite?

SQLite was chosen because it is:

- Lightweight
- Serverless
- Easy to set up
- Stores data inside a single database file
- Perfect for learning backend development and small applications

---

## Database

Database file:

```text
tasks.db
```

When the application starts it automatically:

- Creates the database if it doesn't exist.
- Creates the `tasks` table if it doesn't exist.
- Inserts three sample tasks only if the table is empty.

---

## Project Structure

```text
W3-A1-SQLite-CRUD/
│
├── main.py
├── tasks.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/fast-hashir0729-arch/Internship-Tasks.git
```

Navigate to this assignment:

```bash
cd Connecting-Database
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------------|----------------------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

---

## Example SQL Queries

Retrieve all tasks:

```sql
SELECT * FROM tasks;
```

Retrieve completed tasks:

```sql
SELECT * FROM tasks WHERE done = 1;
```

Count total tasks:

```sql
SELECT COUNT(*) FROM tasks;
```

---

## Database Screenshot

Add your SQLite database screenshot below.

![Database](database.png)

---

## What I Learned

Through this assignment, I learned:

- SQLite fundamentals
- SQL CRUD operations
- Connecting FastAPI with SQLite
- Persistent data storage
- Parameterized SQL queries
- Preventing SQL Injection
- Using `sqlite3` in Python
- CRUD API implementation with a database
- Separation between the API layer and the data layer

---

## Future Improvements

- Search tasks
- Filter completed tasks
- Sorting
- Pagination
- Authentication
- PostgreSQL migration
- SQLAlchemy ORM

---

## Author

**Hashir Ahmed**

Backend Development Internship