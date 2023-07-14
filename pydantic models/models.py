from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: int
    address: str | None = ""

class Cloth(BaseModel):
    name: str
    size: str
    price: float
    discount: float | None = 0