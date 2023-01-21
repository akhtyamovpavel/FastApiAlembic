from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True