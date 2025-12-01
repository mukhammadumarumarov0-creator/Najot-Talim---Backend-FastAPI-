from fastapi import APIRouter
from database.config import SessionClient
from database.models import Comment,User
from database.schemes import CommentData

comment_router=APIRouter()

@comment_router.get("/get_comments")
def get_all_comments():
    with SessionClient() as db:
      comments=db.query(Comment).all()

    message={
        "status":"OK",
        "message":"All comments are fetched successfuly",
        "comments":comments
    }

    return message

@comment_router.post("/create_comment")
def create_comments(comment:CommentData):
   with SessionClient() as db:
      comment=Comment(comment_text=comment.comment_text,user_id=comment.user_id)

      db.add(comment)
      db.commit()
      db.refresh(comment)

   message={
      "status":"OK",
      "message":"comment is created successfuly",
      "comment":comment 
    }
   
   return message

@comment_router.get("/get_user_by_id/{user_id}")
def get_user_by_id(user_id:int):
   with SessionClient() as db:
        stmt=db.query(User).where(User.id==user_id)
        user=db.scalars(stmt).first()

   message={
        "status":"OK",
        "message":"User is fetched seccessfuly",
        "user":user}
   
   return message
   
   
