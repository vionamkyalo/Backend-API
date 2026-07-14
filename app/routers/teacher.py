from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import(
    get_teachers,
    add_teacher,
    update_teacher,
    delete_teacher
)

router =APIRouter(prefix="/teachers",tags=["teachers"])

@router.get("")
def list_teachers():
    teachers= get_teachers()
    return teachers

@router.post("")
def register_teacher(teacher:Teacher):
    add_teacher(teacher.first_name,teacher.last_name,teacher.email,teacher. country,teacher.department,teacher.teacher_id)
    return{"message":"teacher registered", "data":teacher}



@router.put("/{id}")
def edit_teacher(id:int,teacher:Teacher):
    update_teacher(id,teacher.first_name,teacher.last_name,teacher.email,teacher. country,teacher.department,teacher.teacher_id)
    return{"message":"Teacher updated successfully","teacher":teacher}

@router.delete("/{id}")
def remove_teacher(id:int,teacher:Teacher):
    delete_teacher(id)
    return {"message": "Teacher deleted successfully"}