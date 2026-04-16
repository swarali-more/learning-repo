import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(
    0,
    r"C:\swarali\vs code folder\learning-folder\fastapi-learning\practice\02_path_query_params"
)

from params import app

client = TestClient(app)

def test_get_product():
    response = client.get("/product/5")
    assert response.status_code == 200
    assert response.json() == {"product_id": 5}

def test_get_student():
    response = client.get("/student/10")
    assert response.status_code == 200
    assert response.json() == {"Roll_No": 10}

def test_get_city():
    response = client.get("/city/pune")
    assert response.status_code == 200
    assert response.json() == {"City Name":"pune"}