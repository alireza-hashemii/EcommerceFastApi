from db.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    password = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)



class Cloth(Base):
    __tablename__ = "cloth"
    _id = Column(Integer,unique=True,index=True,primary_key=True)
    price = Column(Integer)
    post_number = Column(Integer)
    name = Column(String)
    category = Column(String)
    gender = Column(String)
    detail = Column(String)
    image = Column(String)
