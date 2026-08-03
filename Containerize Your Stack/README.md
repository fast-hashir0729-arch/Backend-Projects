# Containerize Your Stack

A backend REST API built with **FastAPI** and **PostgreSQL**, fully containerized using **Docker** and orchestrated with **Docker Compose**.

This project demonstrates replacing an in-memory data store with a PostgreSQL repository while keeping the service and API layers unchanged through a layered architecture.

---

## Assignment Goal

- Run PostgreSQL inside Docker
- Connect FastAPI to PostgreSQL
- Replace the in-memory repository with a PostgreSQL repository
- Use environment variables for configuration
- Start the entire stack using Docker Compose
- Persist data across container restarts

---

# Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- psycopg2
- Docker
- Docker Compose
- SQL
- python-dotenv

---

# Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── repository.py
│   ├── routes.py
│   ├── schemas.py
│   ├── service.py
│   └── models.py
│
├── sql/
│   └── init.sql
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .env.docker
└── .gitignore
```

---

# Architecture

```
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
PostgreSQL Database
```

The project follows a layered architecture:

- **Routes** handle HTTP requests.
- **Service** contains business logic.
- **Repository** communicates with the database.
- **Database** manages the PostgreSQL connection.

Because of this separation, only the **repository layer** was changed when switching from an in-memory store to PostgreSQL. The service and API routes remained unchanged.

---

# Features

- CRUD API
- PostgreSQL database
- Dockerized application
- Docker Compose orchestration
- Environment variable configuration
- Persistent database storage
- Layered architecture
- SQL initialization script

---

# Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/tasks_db
```

A sample configuration is provided in `.env.example`.

---

# Running with Docker

Clone the repository.

```bash
git clone https://github.com/fast-hashir0729-arch/Internship-Tasks.git/tree/main/CRUD-Operations
```

Move into the project.

```bash
cd Containerize-Your-Stack
```

Start the application.

```bash
docker compose up --build
```

The API will be available at

```
http://localhost:8000
```

Swagger documentation

```
http://localhost:8000/docs
```

---

# Database Initialization

The database schema is automatically created using

```
sql/init.sql
```

when the PostgreSQL container starts for the first time.

---

# Persistence Test

To verify persistence:

1. Start the application

```bash
docker compose up
```

2. Create a record using the API.

3. Stop the containers.

```bash
docker compose down
```

4. Start the containers again.

```bash
docker compose up
```

5. Retrieve the previously created record.

The data remains available because PostgreSQL stores its data inside a Docker volume.

---

# Layered Architecture Demonstration

Originally the application used an in-memory repository.

After introducing PostgreSQL:

✅ Routes remained unchanged

✅ Service layer remained unchanged

✅ Only the repository implementation changed

This demonstrates the benefit of separating business logic from data access.

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

# Docker Services

The project contains two containers.

### FastAPI

- Serves the REST API
- Connects to PostgreSQL

### PostgreSQL

- Stores application data
- Uses a Docker volume for persistence
- Initializes tables using `init.sql`

---

# Learning Outcomes

This project demonstrates:

- Docker fundamentals
- Docker Compose
- PostgreSQL integration
- Environment variables
- Repository Pattern
- Layered Architecture
- SQL initialization
- Data persistence
- Container networking

---

# Future Improvements

- SQLAlchemy ORM
- Alembic migrations
- Redis caching
- Authentication
- Automated testing
- CI/CD pipeline

---

# Author

**Hashir Ahmed**

Computer Science Student | Backend Developer | AI Enthusiast