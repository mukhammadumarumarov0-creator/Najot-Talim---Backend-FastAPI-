from fastapi import FastAPI
from database import Base,engine
from api import blog_router,comment_router,dashboard_router,course_router

app=FastAPI(title="Najot_talim - Backend")

Base.metadata.create_all(bind=engine)

app.include_router(blog_router,prefix="/blogs")
app.include_router(comment_router,prefix="/comments")
app.include_router(dashboard_router,prefix="/dashboards")
app.include_router(course_router,prefix="/course")






