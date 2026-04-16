age = int(input("Enter Your Age:"))
degree=True

if age >=21:
    if degree:
        print("Eligible for job")
    else:
        print("Degree Required")

else:
    print("age is not eligible")