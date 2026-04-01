# Basic Routes - Notes

## What is a Route?
FastAPI मध्ये route म्हणजे एक URL endpoint जो specific function शी connected असतो.

---

## Key Concepts

**1. FastAPI app बनवणे**
`app = FastAPI()` — हे main application object आहे.

**2. GET Route**
`@app.get("/")` — हा decorator route define करतो.
Function return केलेला data JSON format मध्ये येतो.

**3. Multiple Routes**
एका app मध्ये अनेक routes असू शकतात.
प्रत्येक route वेगळ्या URL ला respond करतो.