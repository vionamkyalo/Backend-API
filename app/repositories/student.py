from database import get_db_connection

#students
def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students(name,age,email,country,id_number) VALUES(?,?,?,?,?)',
            (name,age,email,country,id_number),
        )
#return
def get_students():
    with get_db_connection() as connection:
        connection.execute('SELECT*FROM students').fetchall()
        
        
#update
def update_student(student_id,name,age,email,country,):
    with get_db_connection()as connection:
        connection.execute(
        'UPDATE students SET name=?,age=?,email=?,country=?,id_number=? WHERE id=?',
        (name,age,email,country,student_id)
        )
        
        
#delete
def delete_student(student_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?',(student_id))       