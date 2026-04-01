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