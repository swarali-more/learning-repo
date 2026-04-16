word=input("Enter Word = ").lower()
count=0

for i in word:
    if i in "aeiou":
        count+=1

print("Total vowels are =",count)