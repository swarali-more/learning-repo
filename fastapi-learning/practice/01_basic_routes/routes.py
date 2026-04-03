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