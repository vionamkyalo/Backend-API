from pydantic import BaseModel


class Course(BaseModel):
    code: int
    course_name: str
    description: str
    teacher_id: int
