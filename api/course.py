from fastapi import APIRouter
from database.schemes import *
from database.models import Course,Category
from database import SessionClient

course_router=APIRouter()

@course_router.post("/create_course")
def create_course(course:CourseData):
    with SessionClient() as db:
        course_data=Course(
            name=course.name,
            duration=course.
            duration,description=course.description,
            logo_path=course.logo_path,
            technologies=course.technologies,
            price=course.price,
            category_id=course.category_id,
            course_type=course.course_type
            )
        db.add(course_data)
        db.commit()
        db.refresh(course_data)

    message={
        "status":"OK",
        "message":"Course created successfuly",
        "course":course_data
    }

    return message

@course_router.get("/courses")
def get_all_courses():
    with SessionClient() as db:
        courses=db.query(Course).all()
        
    message={
        "status":"OK",
        "message":"All courses fetched successfuly",
        "courses":courses
        }

    return message

@course_router.get("/get_category_by_id/{category_id}")
def get_by_id(category_id:int):
    with SessionClient() as db:
        stmt=db.query(Category).where(Category.id==category_id)
        category=db.scalars(stmt).first()

    message={
        "status":"OK",
        "message":"category is fetched seccessfuly",
        "category":category
    }
    return message

