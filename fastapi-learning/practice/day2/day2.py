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


