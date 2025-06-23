text=(input("enter a string"))
reverse=""
for i in range(len(text)):
    reverse =text[i]+reverse
print("reversed string:",reverse)