from pydantic import BaseModel

class Create_consultation(BaseModel):
    full_name:str
    phone_number:str

class CourseData(BaseModel):
    name:str
    duration:int
    description:str
    logo_path:str
    technologies:str
    price:int
    category_id:int
    course_type:str

class BlogData(BaseModel):
    title:str
    image_path:str
    content:str
    category_id:int

   
class CommentData(BaseModel):
    comment_text:str
    user_id:int
