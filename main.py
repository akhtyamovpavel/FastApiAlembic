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
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User elready exist')
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
