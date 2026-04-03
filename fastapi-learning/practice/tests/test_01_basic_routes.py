import sys
import pytest
from fastapi.testclient import TestClient

import sys

sys.path.append(r"C:\swarali\vs code folder\learning-folder\fastapi-learning\practice\01_basic_routes")

from routes import app

client = TestClient(app)

# Test 1: Home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

# Test 2: About route
def test_about():
    response = client.get("/about")
    assert response.status_code == 200

# Test 3 - User (Path Parameter)
def test_get_user():
    response = client.get("/user/5")
    assert response.status_code == 200
    assert response.json() == {"user_id": 5}

# Test 4 - Book (Path Parameter)
def test_get_book():
    response = client.get("/book/Harry Potter")
    assert response.status_code == 200
    assert response.json() == {"book_name": "Harry Potter"}

# Test 5 - Products ( Query Parameter)
def test_get_products():
    response = client.get("/products?category=electronics&price=500")
    assert response.status_code == 200
    assert response.json() == {"category": "electronics", "price": 500}

# Test 6 - Students ( Query Parameter)
def test_get_students():
    response = client.get("/students?name=Swarali&age=20")
    assert response.status_code == 200
    assert response.json() == {"name": "Swarali", "age": 20}

# Test 7 - Orders (Both (Path + Query))
def test_get_order():
    response = client.get("/order/101?status=delivered")
    assert response.status_code == 200
    assert response.json() == {"order_id": 101, "status": "delivered"}