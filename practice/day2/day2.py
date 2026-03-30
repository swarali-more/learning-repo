from fastapi import FastAPI

app = FastAPI()


#Path Parameter
@app.get("/product/5")
def get_product():
    return {"product_id": 5}
#... 1000 products असतील तर? 😱
#Solution = Path Parameter!

#Product_Id
@app.get("/product/{product_id}")
def get_product(product_id : int):
    return {"product_id": product_id}

#Task: 1
#Roll No.
@app.get("/student/{roll_no}")
def get_rollno(roll_no : int):
    return {"Roll_No": roll_no}

#Task: 2
#City_Name
@app.get("/city/{city_name}")
def get_city_name(city_name : str):
    return {"City Name" : city_name}

#Task: 3
#User_Id_Profile
@app.get("/user/{user_id}/profile")
def get_user_id(user_id : int):
    return {"User Info":f"Profile of user {user_id}"}




#Query Parameter
@app.get("/search")
def search(name: str):
    return {"search": name}

#Query Parameter With Defaul Value
@app.get("/search")
def search(name: str = "Guest"):  #default value
    return {"search": name}       #our value

#Item Limits
@app.get("/items")
def get_items(limit: int = 10,skip: int = 0):
    return {"Limit": limit, "Skip": skip}

#Task: 1
#Students Class and Subjects
@app.get("/students")
def get_students(collage_name: str , subject: str = "all"):
    return {"Collage_Name":collage_name,"Subject":subject}

#Task: 2
#Products
@app.get("/product")
def get_product(category: str,price: int = 100,discount: bool = False):
    return {"Category":category, "Price": price ,"Discount": discount}



#Path + Query
#User_Post_Limit
@app.get("/user/{user_id}/posts")
def get_user_posts(user_id: int, limit: int = 5):
    return {"User_Id": user_id , "Limit": limit}

#Task: 1
#Shop_Product_limit
@app.get("/shop/{shop_id}/products")
def shop_info(shop_id: int , limit: int = 5 , discount: bool = False ):
    return {"Shop_Id": shop_id , "Limit": limit , "Discount": discount}