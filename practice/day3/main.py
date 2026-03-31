from fastapi import FastAPI
from day3.schemas import Item

app = FastAPI()

# -- Phase 1: Basic Pydantic Model --

@app.post("/items/")
async def create_item(item: Item):
    return {
        "message": "Item created successfully!",
        "item_name": item.name,
        "item_price": item.price,
        "in_stock": item.in_stock
    }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "updated_item": item
    }

@app.get("/items/")
async def get_all_items():
    return {
        "message": "All items fetched!"
    }