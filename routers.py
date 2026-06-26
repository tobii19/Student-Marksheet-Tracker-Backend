from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import Students
from schemas import Create_Student,Show_Student,Update_Student
 
router = APIRouter(prefix="/students",tags=["Student"])

@router.post("/add_stu",response_model = Show_Student)
def add_stu(stu : Create_Student,db : Session = Depends(get_db)):
    db_stu = db.query(Students).filter(Students.email == stu.email).first()
    
    if db_stu:
        raise HTTPException(status_code=404,detail="User Alreay Exists")
    
    total = stu.science + stu.maths + stu.english
    
    percentage = total/3
    
    if stu.science > 35 and stu.maths > 35 and stu.english > 35 and percentage > 34:
        result = "Pass"
    else: 
        result = "Fail"
    
    new_stu = Students(
        fname=stu.fname,
        email=stu.email,
        course=stu.course,
        maths=stu.maths,
        science = stu.science,
        english = stu.english,
        percentage = percentage,
        result = result
    )
    
    db.add(new_stu)
    db.commit()
    db.refresh(new_stu)
    
    return new_stu

@router.get("/show_stu/{id}",response_model = Show_Student)
def show_stu(id : int,db : Session = Depends(get_db)):
    new_user = db.query(Students).filter(Students.id == id).first()
    
    if not new_user:
        raise HTTPException(status_code=404,detail="Student Not Found")
    
    return new_user

@router.put("/update_stu/{stu_id}",response_model=Show_Student)
def update_stu(stu_id : int,stu : Update_Student,db : Session = Depends(get_db)):
    db_user = db.query(Students).filter(Students.id == stu_id).first()
    
    if not db_user:
        raise HTTPException(status_code=404,detail="User not Found")

    db_user.fname = stu.fname 
    db_user.email = stu.email
    db_user.course = stu.course
    db_user.maths = stu.maths
    db_user.english = stu.english
    db_user.science = stu.science
    db_user.percentage = (stu.science + stu.maths + stu.english)/3
    if stu.science > 35 and stu.maths > 35 and stu.english > 35 and ((stu.science + stu.maths + stu.english)/3) > 35:
        db_user.result = "Pass"
    else: 
        db_user.result = "Fail"
    
    
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.delete("/delete/{stu_id}")
def delete_stu(stu_id : int,db : Session =Depends(get_db)):
    
    db_stu = db.query(Students).filter(Students.id == stu_id).first()
    
    if not db_stu:
        raise HTTPException(status_code=404,detail="Student Not Exists")
    db.delete(db_stu)
    db.commit()
    return "Student Deleted Successfully"
