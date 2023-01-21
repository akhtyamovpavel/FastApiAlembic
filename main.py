from typing import List
from fastapi import Depends, FastAPI, HTTPException

from db import Base, SessionLocal, engine
import schemas
from sqlalchemy.orm import Session
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/user', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User elready exist')
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post('/student', response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db, student=student)
    return db_student


@app.get('/student', response_model=List[schemas.Student])
async def get_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    print(students)
    return students
