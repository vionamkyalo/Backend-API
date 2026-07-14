from fastapi import APIRouter
from schemas.course import Course
from repositories.course import (
    get_courses,
    add_course,
    update_course,
    delete_course
)
router =APIRouter(prefix="/course",tags=["courses"])


@router.get("/")
def list_courses():
    courses=get_courses()
    return courses

@router.post("")
def register_course(course:Course):
    add_course(course.code,course.course_name,course.description,course.teacher_id)
    return{"message":"course registered", "data":course}

@router.put("{courses_id}")
def edit_courses(id:int, course: Course):
    update_course(id,course.code,course.course_name,course.description,course.teacher_id)
    return {"message": "Course updated successfully", "course": Course}


@router.delete("{courses_id}")
def remove_course(id:int, course:Course):
    delete_course(id)
    return {"message": "Course deleted successfully"}