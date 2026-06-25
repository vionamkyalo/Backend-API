from database import (create_table, add_student,get_students,update_student,
                      delete_student,add_teacher,get_teachers,update_teacher,delete_teacher,
                      add_course, get_courses,update_course, delete_course)
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Student(BaseModel):
    name:str # this formart of code writing is called type hint
    age:int
    email:str
    country:str
    id_number:int


@app.get("/students")
def home():
    return {"message":"welcome to my first server"}

create_table()
@app.get("/students")
def list_students():
    students=get_students()
    return students


create_table()
@app.post("/students")
def register_student(student:Student):
    add_student(student.name,student.age,student.email,student.country,student.id_number)
    return {"message":"student registered", "student":student}


@app.put("/students/{id}")
def modify_student(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully", "student_id": id,"updated_data":student}


@app.delete("/students/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "Student deleted successfully"}

class Teacher(BaseModel):
    first_name:str
    last_name:str
    email:str
    country:str
    department:str
    teacher_id:int

@app.get("/teachers")
def list_teachers():
    teachers= get_teachers()
    return teachers

@app.post("/teachers")
def register_teacher(teacher:Teacher):
    add_teacher(teacher.first_name,teacher.last_name,teacher.email,teacher. country,teacher.department,teacher.teacher_id)
    return{"message":"teacher registered", "data":teacher}



@app.put("/teachers/{id}")
def edit_teacher(id:int,teacher:Teacher):
    update_teacher(id,teacher.first_name,teacher.last_name,teacher.email,teacher. country,teacher.department,teacher.teacher_id)
    return{"message":"Teacher updated successfully","teacher":teacher}

@app.delete("/teachers/{id}")
def remove_teacher(id:int,teacher:Teacher):
    delete_teacher(id)
    return {"message": "Teacher deleted successfully"}


class Course(BaseModel):
    code:int
    course_name:str
    description:str
    teacher_id:int

@app.get("/Course")
def list_courses():
    courses=get_courses()
    return courses

@app.post("/Course")
def register_course(course:Course):
    add_course(course.code,course.course_name,course.description,course.teacher_id)
    return{"message":"course registered", "data":course}

@app.put("/courses/{id}")
def edit_courses(id:int, course: Course):
    update_course(id,course.code,course.course_name,course.description,course.teacher_id)
    return {"message": "Course updated successfully", "course": Course}


@app.delete("/courses/{id}")
def remove_course(id:int, course:Course):
    delete_course(id)
    return {"message": "Course deleted successfully"}

