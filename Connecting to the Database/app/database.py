import sqlite3

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
    cursor.execute(
        'INSERT INTO tasks (title, done) VALUES ("Study FastAPI", False)'
    )
    cursor.execute(
        'INSERT INTO tasks (title, done) VALUES ("Go to the gym", True)'
    )
    cursor.execute(
        'INSERT INTO tasks (title, done) VALUES ("Complete internship assignment", False)'
    )
    connection.commit()