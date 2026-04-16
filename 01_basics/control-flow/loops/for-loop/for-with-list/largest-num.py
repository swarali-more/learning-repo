list1=[10,20,30,40,50]

largest=list1[0]
second=list1[0]

for i in list1:
    if i > largest:
        second = largest
        largest=i 
    elif i > second and i != largest:
        second = i
        
print(largest)
print(second)

         
