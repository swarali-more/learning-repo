# BaseModel

# step1:
python -> from practice.day3 import Item  
-> create instance of model and use with different functions

# Test_Cases:

# Case 1: correct_data
abc = Item(name="Laptop", price=999.99)
print(abc)

# o/p -> name='Laptop' price=999.99 description=None in_stock=True
note: optional fields aaplach default value gheta  
- description=None, in_stock=True

# Case 2: wrong_data
abc2 = Item(name="Laptop", price="wrong_data")

# o/p -> ValidationError: price must be a valid number
note: Pydantic wrong type pakadto ani error deto

# Case 3: model_dump()
abc3 = Item(name="Laptop", price=999.99)
print(abc3.model_dump())

# o/p -> {'name': 'Laptop', 'price': 999.99, 'description': None, 'in_stock': True}
note: Object la dict madhe convert karto

# Case 4: exclude_unset=True
abc4 = Item(name="Laptop", price=999.99)
print(abc4.model_dump(exclude_unset=True))

# o/p -> {'name': 'Laptop', 'price': 999.99}
note: description ani in_stock dila nahi  
to exclude_unset=True mule output madhe ala nahi.  
Sirf explicitly dilele fields return zale.