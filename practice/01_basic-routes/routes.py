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