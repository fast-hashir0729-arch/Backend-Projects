# Week 3 - Assignment 1: Task API with SQLite

## Overview

This project is a RESTful CRUD API built using **FastAPI** and **SQLite**.

Unlike the previous version where everything was implemented inside a single `main.py` file, this project follows a **modular architecture** by separating the application into different layers such as services, repositories, database configuration, and schemas.

The API functionality remains exactly the same while the codebase is now cleaner, easier to maintain, and scalable for future development.

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
- Modular project structure following separation of concerns

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
Connecting-Database/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── repository.py
│   ├── schemas.py
│   └── service.py
│
├── sql/
│   └── init.sql
│
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── tasks.db
```

---

## Project Architecture

The application follows a layered architecture:

- **main.py** → Entry point of the application.
- **database.py** → Handles database connection and initialization.
- **repository.py** → Performs all database operations (CRUD queries).
- **service.py** → Contains the business logic.
- **schemas.py** → Defines request and response models using Pydantic.
- **init.sql** → Creates the database schema during initialization.

This separation makes the project easier to maintain, test, and extend.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/fast-hashir0729-arch/Internship-Tasks.git/tree/main/Connecting%20to%20the%20Database
```

Navigate to this assignment:

```bash
cd Connecting-Database
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
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
- Designing a layered backend architecture
- Separation of concerns
- Repository-Service design pattern
- Organizing FastAPI applications into modules

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