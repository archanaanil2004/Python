string=int(input("enter a number"))
length=len(str(string))
print(length)
a=0
if string>=0:
    for i in range(length):
    
        digit =string%10
        a=(a*10)+digit
        string=string//10
    print(a)    
else: 


    print("not equal")  