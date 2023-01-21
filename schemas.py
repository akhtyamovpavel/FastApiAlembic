from pydantic import BaseModel

import models


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True


class Student(BaseModel):
    user: User
    group_number: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    user_id: int
    group_number: str
