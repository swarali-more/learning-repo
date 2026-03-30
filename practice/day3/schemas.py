from pydantic import BaseModel, Field
from typing import Optional

#--Phase 1: Basic Pydantic Model--

class Item(BaseModel):
    name:str
    price:float
    description:Optional[str]= None
    in_stock:bool=True