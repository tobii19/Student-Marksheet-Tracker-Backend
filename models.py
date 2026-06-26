from sqlalchemy import Column,String,Integer,String,Float
from db import Base

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    fname = Column(String,nullable=False,index=True)
    email = Column(String,unique=True,index=True)
    course = Column(String)
    english = Column(Integer)
    science = Column(Integer)
    maths = Column(Integer)
    percentage = Column(Float)
    result = Column(String)