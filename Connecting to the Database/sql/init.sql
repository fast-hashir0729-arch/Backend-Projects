CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO tasks (title, done)
SELECT 'Study FastAPI', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Study FastAPI'
);

INSERT INTO tasks (title, done)
SELECT 'Go to the gym', TRUE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Go to the gym'
);

INSERT INTO tasks (title, done)
SELECT 'Complete internship assignment', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Complete internship assignment'
);