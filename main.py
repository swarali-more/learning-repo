from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello There"}


@app.get("/about")
def about():
    return {"message":"I am Swarali, Python Backend Developer!"}

@app.get("/user/{name}")
def get_user(name:str):
    return {"message":f"Hello {name},Welcome to mt API !"}

    
@app.get("/multiply/{x}/{y}")
def multi(x:int,y:int):
    return {"result": x * y}


@app.get("/skills")
def skills():
    return {"skills": ["Python", "FastAPI", "Git", "React"]}