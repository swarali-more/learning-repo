from fastapi import FastAPI

app = FastAPI()

#route 1 - Home
@app.get("/")
def home():
    return {"message":"Hello World!"}

#route 2 - About
@app.get("/about")
def about():
    return{"message:" "I am learning FastAPI!"}

# Route 3 - User
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Route 4 - Book
@app.get("/book/{book_name}")
def get_book(book_name: str):
    return {"book_name": book_name}

# Route 5 - Products
@app.get("/products")
def get_products(category: str, price: int):
    return {"category": category, "price": price}

# Route 6 - Students
@app.get("/students")
def get_students(name: str, age: int):
    return {"name": name, "age": age}

# Route 7 - Orders
@app.get("/order/{order_id}")
def get_order(order_id: int, status: str):
    return {"order_id": order_id, "status": status}