from pydantic import BaseModel,EmailStr
from typing import Optional

class Create_Student(BaseModel):
    id : int
    fname : str
    email : EmailStr
    course : str
    english : int
    science : int
    maths : int
  
    
    
class Show_Student (BaseModel):
    id : int
    fname : str
    email : EmailStr
    course : str
    english : int
    science : int
    maths : int
    percentage : float
    result : str
    
class Update_Student(BaseModel):
    fname: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None
    maths: Optional[int] = None
    science: Optional[int] = None
    english: Optional[int] = None
    