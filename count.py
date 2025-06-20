i = int(input("Enter a number: "))
j = 0
a = i
while a>0:
    a=a//10
    j=j+1
if i==0:
    j=1
print("print number of digits:",j)