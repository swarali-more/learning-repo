# Pydantic BaseModel - Notes

## What is BaseModel?
Pydantic चा BaseModel वापरून data validation करता येतो.
Wrong type दिलं तर आपोआप ValidationError येतो.

---

## Key Concepts

**1. Optional Fields**
Fields ला default value दिली तर ती automatically set होते.
- `description = None` by default
- `in_stock = True` by default

**2. ValidationError**
Wrong type दिला तर Pydantic लगेच error देतो.
Example: price मध्ये string दिलं तर `ValidationError` येतो.

**3. model_dump()**
Pydantic object ला Python dictionary मध्ये convert करतो.

**4. exclude_unset=True**
`model_dump()` मध्ये फक्त explicitly दिलेले fields return होतात.
Default values exclude होतात.