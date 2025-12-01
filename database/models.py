from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Text,INTEGER,ForeignKey,Enum,DateTime,func
from .config import Base
import enum
from datetime import datetime

class FreeConsultation(Base):
    __tablename__="free_consultation"

    id:Mapped[int]=mapped_column(primary_key=True)
    full_name:Mapped[str]=mapped_column(String(200))
    phone_number:Mapped[str]=mapped_column(String(13))


    def __repr__(self):
        return self.full_name
    
    
class CaruselAd(Base):
    __tablename__="carusel_ad"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(200))
    description:Mapped[str]=mapped_column(Text)

    def __repr__(self):
        return self.title


class Category(Base):
    __tablename__="category"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))

    course:Mapped[list["Course"]]=relationship(back_populates="category")
    blog:Mapped[list["Blog"]]=relationship(back_populates="catagory")

    def __repr__(self):
        return self.name

class CourseTypeChoies(str,enum.Enum):
    STANDART="Standart"
    BOOTCAMP="Bootcamp"
    OTHER="Other"

class Course(Base):
    __tablename__="courses"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    duration:Mapped[int]=mapped_column(INTEGER())
    description:Mapped[str]=mapped_column(Text())
    logo_path:Mapped[str]=mapped_column(String(200))
    technologies:Mapped[str]=mapped_column(Text())
    price: Mapped[int]=mapped_column(INTEGER())
    category_id:Mapped[int]=mapped_column(INTEGER(),ForeignKey("category.id"))
    course_type:Mapped[str]=mapped_column(Enum(CourseTypeChoies),default=CourseTypeChoies.STANDART)

    category:Mapped["Category"]=relationship(back_populates="course")

    def __repr__(self):
        return self.name


class Blog(Base):
    __tablename__="blogs"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(100))
    image_path:Mapped[str]=mapped_column(String(200))
    content : Mapped[str]=mapped_column(Text)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=func.now())
    views : Mapped[int]=mapped_column(INTEGER(),default=0)
    category_id:Mapped[int]=mapped_column(INTEGER(),ForeignKey("category.id"))

    catagory:Mapped["Category"]=relationship(back_populates="blog")

class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(200))
    job:Mapped[str]=mapped_column(String(100),default="Unknown")

    comment:Mapped[list["Comment"]]=relationship(back_populates="user")

class Comment(Base):
    __tablename__="comments"

    id:Mapped[int]=mapped_column(primary_key=True)
    comment_text:Mapped[str]=mapped_column(Text)
    user_id:Mapped[int]=mapped_column(INTEGER(),ForeignKey("users.id"))

    user:Mapped["User"]=relationship(back_populates="comment")

