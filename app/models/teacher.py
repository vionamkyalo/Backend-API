from database import get_db_connection


def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           first_name TEXT NOT NULL,
                           last_name TEXT NOT NULL,
                           email TEXT UNIQUE NOT NULL,
                           country TEXT NOT NULL,
                           departement TEXT NOT NULL
                           )''')