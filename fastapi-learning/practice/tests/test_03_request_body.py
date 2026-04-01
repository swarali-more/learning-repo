import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, r"C:\swarali\vs code folder\lerning-folder\fastapi-lerning\practice\03_request-body-pydantic")

from main import app

client = TestClient(app)

# Test 1: Create item - POST
def test_create_item():
    response = client.post("/items/", json={
        "name": "Laptop",
        "price": 999.99,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["item_name"] == "Laptop"
    assert response.json()["item_price"] == 999.99

# Test 2: Get all items - GET
def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200

# Test 3: Update item - PUT
def test_update_item():
    response = client.put("/items/1", json={
        "name": "Updated Laptop",
        "price": 1299.99,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["item_id"] == 1