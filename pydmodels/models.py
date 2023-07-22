from pydantic import BaseModel  


class User(BaseModel):
    name: str
    email: str
    password: int
    address: str | None = ""

# class Choices(enum.Enum):
#     f = 'f'
#     m = 'm'

# class Category(enum.Enum):
#     pants = 'pants'
#     jacket = 'jacket'
#     shirt = "shirt"


# class ClothScheme(BaseModel):
    
#     model_config = ConfigDict(from_attributes=True)
#     price : float
#     gender :  str
#     name : str 
#     detail : str 
#     category : str

