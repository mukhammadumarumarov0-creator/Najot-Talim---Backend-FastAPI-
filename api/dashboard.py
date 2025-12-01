from fastapi import APIRouter
from database import SessionClient
from sqlalchemy.orm import joinedload
from database.models import CaruselAd,FreeConsultation
from database.schemes import *
from pydantic import BaseModel

dashboard_router=APIRouter()



@dashboard_router.get("/carusel")
def get_carusel():
    with SessionClient() as db:
        data=db.query(CaruselAd).all()
        message ={
            "status":True,
            "message":"all carusel data fetched",
            "data": data
        }
        return message
   
    
@dashboard_router.post("/consult")
def create_user(user:Create_consultation):

    with SessionClient() as db:
        const=FreeConsultation(full_name=user.full_name,phone_number= user.phone_number)

        db.add(const)
        db.commit()
        db.refresh(const)

        message={
            "status": "OK",
            "message" : "Cansultation created successfuly",
            "user": const
        }

        return message



