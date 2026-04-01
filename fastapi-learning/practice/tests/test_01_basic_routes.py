import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, r"C:\swarali\vs code folder\lerning-folder\fastapi-lerning\practice\01_basic-routes")

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