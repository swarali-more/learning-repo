from pydantic import BaseModel, EmailStr
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

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "Gaming laptop",
                "price": 75000,
                "in_stock": True
            }
        }