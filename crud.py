from sqlalchemy.orm import Session

import models
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).all()


def get_students(db: Session):
    students = db.query(models.Student).all()
    return students


def create_student(db: Session, student: schemas.StudentCreate):

    user = db.query(models.User).get(student.user_id)
    db_student = models.Student(
        user=user,
        group_number=student.group_number
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
