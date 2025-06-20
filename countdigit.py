i = int(input("Enter a number: "))
j = int(input("Enter the digit to count: "))
a = 0
b= i

while b > 0:
    c = b % 10
    if c == j:
        a+= 1
    b=b // 10
if i==0 and j==0:
    a=1   

print("count of digits=",a)