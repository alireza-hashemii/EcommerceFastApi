from pydantic import BaseModel , FilePath  
import random
import enum

class User(BaseModel):
    name: str
    email: str
    password: int
    address: str | None = ""

class Choices(enum.Enum):
    f = 'f'
    m = 'm'

class Category(enum.Enum):
    pants = 'pants'
    jacket = 'jacket'
    shirt = "shirt"


class PCloth(BaseModel):
    price : float
    gender :  Choices
    name : str | None = None
    detail : str 
    category : Category
    image : FilePath
