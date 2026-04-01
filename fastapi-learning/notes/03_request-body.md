# Request Body - Notes

## What is Request Body?
Client कडून server ला data पाठवणे — POST, PUT requests मध्ये वापरतात.

---

## Key Concepts

**1. POST Route**
`@app.post("/items/")` — नवीन data create करायला वापरतात.
Request body मधून Item object येतो.

**2. PUT Route**
`@app.put("/items/{item_id}")` — existing data update करायला वापरतात.
Path param + request body दोन्ही येतात.

**3. Pydantic Model**
Request body validate करायला Pydantic model वापरतात.
Wrong data आलं तर automatically error येतो.