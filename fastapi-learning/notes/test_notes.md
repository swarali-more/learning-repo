# 🧪 FastAPI - Testing Notes

## ⚙️ Setup (सर्व test files मध्ये same)

```python
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, r"C:\...\practice\01_basic_routes")  # file location सांगतो
from routes import app       # आपला FastAPI app import

client = TestClient(app)     # test client बनवतो
```

> `TestClient` → FastAPI चा built-in testing tool (Starlette वर based)

---

## 📁 Test File 1 — `test_01_basic_routes.py`

**काय test केलं:** Basic GET routes — Home, About, Path Params, Query Params

| Test | Route | Check |
|------|-------|-------|
| `test_home` | `GET /` | `{"message": "Hello World!"}` |
| `test_about` | `GET /about` | status 200 |
| `test_get_user` | `GET /user/5` | `{"user_id": 5}` |
| `test_get_book` | `GET /book/Harry Potter` | `{"book_name": "Harry Potter"}` |
| `test_get_products` | `GET /products?category=electronics&price=500` | category + price check |
| `test_get_students` | `GET /students?name=Swarali&age=20` | name + age check |
| `test_get_order` | `GET /order/101?status=delivered` | path + query दोन्ही |

**Key concept:**
```python
response = client.get("/user/5")
assert response.status_code == 200
assert response.json() == {"user_id": 5}
```

---

## 📁 Test File 2 — `test_02_path_query_params.py`

**काय test केलं:** Path Parameters → product, student, city

| Test | Route | Check |
|------|-------|-------|
| `test_get_product` | `GET /product/5` | `{"product_id": 5}` |
| `test_get_student` | `GET /student/10` | `{"Roll_No": 10}` |
| `test_get_city` | `GET /city/Pune` | `{"City Name": "Pune"}` |

**Key concept:**
```python
# Path parameter → URL मध्येच value टाकतो
response = client.get("/city/Pune")
assert response.json() == {"City Name": "Pune"}
```

---

## 📁 Test File 3 — `test_03_request_body.py`

**काय test केलं:** POST, GET, PUT → Items CRUD

| Test | Method + Route | Check |
|------|---------------|-------|
| `test_create_item` | `POST /items/` | item_name + item_price |
| `test_get_all_items` | `GET /items/` | status 200 |
| `test_update_item` | `PUT /items/1` | item_id == 1 |

**Key concept:**
```python
# POST → json={} म्हणजे request body पाठवतो
response = client.post("/items/", json={
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True
})
assert response.json()["item_name"] == "Laptop"

# PUT → update करताना item id URL मध्ये
response = client.put("/items/1", json={
    "name": "Updated Laptop",
    "price": 1299.99,
    "in_stock": True
})
assert response.json()["item_id"] == 1
```

---

## 💡 Quick Revision

| Concept | Example |
|---------|---------|
| GET request test | `client.get("/path")` |
| POST with body | `client.post("/path", json={...})` |
| PUT update | `client.put("/path/id", json={...})` |
| Status check | `assert response.status_code == 200` |
| JSON check | `assert response.json() == {...}` |
| Key check | `assert response.json()["key"] == value` |

