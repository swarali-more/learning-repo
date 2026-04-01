from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str