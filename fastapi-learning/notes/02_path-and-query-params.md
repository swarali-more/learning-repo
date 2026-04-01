# Path & Query Parameters - Notes

## What are Path Parameters?
URL मध्येच value pass करणे — `"/product/{product_id}"`
Dynamic URLs साठी वापरतात.

---

## Key Concepts

**1. Path Parameter**
`@app.get("/product/{product_id}")` — URL मधून value येते.
Function मध्ये type define करतात — `product_id: int`

**2. Query Parameter**
URL मध्ये `?` नंतर येतो — `"/items?skip=0&limit=10"`
Optional असतो — default value देता येते.

**3. फरक**
- Path param → URL चा भाग असतो
- Query param → URL नंतर `?` ने येतो