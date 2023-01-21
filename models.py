from sqlalchemy import VARCHAR, Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String)
    password_hash = Column(String)
    email = Column(VARCHAR(50))