from database import get_db_connection

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                        code INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        credits INTEGER NOT NULL,
                        description TEXT,
                        teacher_id INTEGER,
                        FOREIGN KEY(teacher_id) REFERENCES teachers(id))''')