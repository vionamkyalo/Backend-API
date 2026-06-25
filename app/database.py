import sqlite3
from contextlib import contextmanager

sqlite_file_name ="school.db"
@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL)''')
        

        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           first_name TEXT NOT NULL,
                           last_name TEXT NOT NULL,
                           email TEXT UNIQUE NOT NULL,
                           country TEXT NOT NULL,
                           departement TEXT NOT NULL
                           )''')
        

        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           code INTEGER NOT NULL,
                           title TEXT NOT NULL,
                           credits INTEGER NOT NULL,
                           description TEXT,
                           teacher_id INTEGER,
                           FOREIGN KEY(teacher_id) REFERENCES teachers(id))''')
        
#students
def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students(name,age,email,country,id_number) VALUES(?,?,?,?,?)',
            (name,age,email,country,id_number),
        )
#returnS
def get_students():
    with get_db_connection() as connection:
        connection.execute('SELECT*FROM students').fetchall()
              
#    #return 
    
# def get_students(students_id):
#     with get_db_connection()as connection:
#         connection.execute('SELECT * FROM students WHERE id =?',(students_id,)).fetchone()
        
        
#update
def update_student(student_id,name,age,email,country,):
    with get_db_connection()as connection:
        connection.execute(
        'UPDATE students SET name=?,age=?,email=?,country=?WHERE id=?',
        (name,age,email,country,student_id)
        )
        
#delete
def delete_student(student_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?',(student_id))


#teachers
def add_teacher(first_name,last_name, email, country,department ):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO teachers(first_name,last_name,email,country,department) VALUES(?,?,?,?,?)',
            (first_name,last_name,email,country,department),
        )

def get_teachers():
    with get_db_connection() as connection:
        connection.execute('SELECT*FROM teachers').fetchall()
    #return 
    
def get_teacher(teacher_id):
    with get_db_connection()as connection:
        connection.execute('SELECT * FROM teachers WHERE id =?',(teacher_id,)).fetchone()



#update
def update_teacher(teacher_id,first_name,last_name,email,country,department):
    with get_db_connection()as connection:
        connection.execute(
        'UPDATE teachers SET first_name=?,last_name=?,email=?,country=?department=? WHERE id=?',
        (first_name,last_name,email,country,department,teacher_id)
        )


#delete
def delete_teacher(teacher_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id=?',(teacher_id))



#courses
def add_course(code,title,credits, description,teacher_id):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO courses(code,title,credits,description,teacher_id) VALUES(?,?,?,?,?)',
            (code,title,credits,description,teacher_id),
        )

def get_courses():
    with get_db_connection() as connection:
        connection.execute('SELECT*FROM courses').fetchall()

 #return
def get_course(course_id):
    with get_db_connection() as connection:
        return connection.execute('SELECT*FROM courses WHERE id=?', (course_id,)).fetchone()
    
#update
def update_course(course_id,code,title,credits,description,teacher_id):
    with get_db_connection()  as connection:
        connection.execute(
            'UPDATE courses SET code=?,title=?,credits=?,description=?,teacher_id=? WHERE id=?',
            (code,title,credits,description,teacher_id,course_id)
        )


#delete
def delete_course(course_id):
    with get_db_connection() as connectiion:
        connectiion.execute('DELETE FROM courses WHERE id=?',(course_id))
        