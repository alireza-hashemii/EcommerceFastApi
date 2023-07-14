from db.database import Base
from sqlalchemy import Boolean, Column, Integer, String 

class User(Base):
    __tablename__ = "users"
    password = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
