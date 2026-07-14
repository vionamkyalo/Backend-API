from database import get_db_connection


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