from typing import Union
from pydantic import BaseModel

import models


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str
    first_name: str


class User(UserBase):
    id: int
    first_name: Union[str, None]
    class Config:
        orm_mode = True


class Student(BaseModel):
    user: User
    group_number: str
    id: int

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    user_id: int
    group_number: str
