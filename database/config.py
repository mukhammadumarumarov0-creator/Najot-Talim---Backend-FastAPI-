from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL="sqlite:///./najot_talim.db"

engine=create_engine(DATABASE_URL)

SessionClient=sessionmaker(bind=engine,autoflush=False)

class Base(DeclarativeBase):
    pass