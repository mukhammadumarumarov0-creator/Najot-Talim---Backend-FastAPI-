from fastapi import APIRouter
from database.schemes import BlogData
from database import SessionClient
from database.models import Blog,Category
blog_router=APIRouter()



@blog_router.get("/get_blogs")
def get_all_blogs():
    with SessionClient() as db:
        blogs=db.query(Blog).all()
    
    message={
        "status":"OK",
        "message":"All blogs are fetched successfuly",
        "blogs":blogs
    }
    return message


@blog_router.post("/create_blog")
def create_blog(blog_d:BlogData):
    with SessionClient() as db:
        blog=Blog(
            title=blog_d.title,
            image_path=blog_d.image_path,
            content=blog_d.content,
            category_id=blog_d.category_id
        )

        db.add(blog)
        db.commit()
        db.refresh(blog)
    message={
        "status":"OK",
        "message":"Blog created successfuly",
        "blog":blog
    }
    return message
    
