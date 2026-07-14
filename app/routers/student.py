from fastapi import APIRouter
from schemas.student import Student
from repositories.student import(
    add_student,
    update_student,
    delete_student,
    get_students
)

router =APIRouter(prefix="/students",tags=["students"])

@router.get("")
def home():
    return {"message":"welcome to my first server"}


@router.get("")
def list_students():
    students=get_students()
    return students


@router.post("")
def register_student(student:Student):
    add_student(student.name,student.age,student.email,student.country,student.id_number)
    return {"message":"student registered", "student":student}



@router.put("/{id}")
def modify_student(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully", "student_id": id,"updated_data":student}


@router.delete("/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "Student deleted successfully"}