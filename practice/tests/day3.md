#BaseModel:

#Phase : 1


#step1:python-->from practice.day3 import Item-->create instance of model use with different funstions

#Test_Cases:

#Case 1:correct data
abc=Item(name="Laptop" , price = 999.99)
print(abc)
o/p--> name='Laptop' price=999.99 des cription=None in_stock=True
note:Optional fields aaplach default value gheta — description=None, in_stock=True

#Case 2: wrong data
abc2=Item(name="Latop" , price="wrong_data")
o/p--> ValidationError: price must be a valid number
note:Pydantic wrong type pakadto aani lगेच error deto

#Case 3: model_dump()
abc3=Item(name="Laptop" , price =999.99)
print(abc3.model_dump())
o/p--> {'name': 'Laptop', 'price': 999.99, 'description': None, 'in_stock': True}
note: Object la dict madhe convert karto

#Case 4:exclude_unset=True
abc4=Item(name="Laptop" , price=999.99)
print(abc4.model_dump(exclude_unset=True))
o/p--> {'name': 'Laptop', 'price': 999.99}
note:description aani in_stock dila nahi — to exclude_unset=True mule output madhe aala nahi. Sirf explicitly dileले fields return zale.