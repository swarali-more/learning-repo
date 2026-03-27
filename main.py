# Daily GitHub commit for contribution graph



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
     return {
        "message": "Hello Swarali 👋",
        "project": "FastAPI Learning",
        "status": "Running successfully"
    }


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

@app.get("/health")
def health():
    return {"status": "API is healthy"}

@app.get("/skills")
def skills():
    return {
        "skills": ["Python", "FastAPI", "Git", "React"]
    }

@app.get("/search")
def search(q: str):
    return {"search_query": q}