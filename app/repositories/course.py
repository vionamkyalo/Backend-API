from database import get_db_connection


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