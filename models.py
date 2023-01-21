from sqlalchemy import VARCHAR, Column, Integer, String, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String)
    password_hash = Column(String)
    email = Column(VARCHAR(50))

    first_name = Column(String)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    group_number = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")

    def __repr__(self) -> str:
        return f'{self.id} - {self.user_id} - {self.group_number}'
