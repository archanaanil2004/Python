i = int(input("Enter a number: "))
j=10
b=i
while(b>0):
    a=(b%10)
    j=(j*10)+a
    b=b//10
if(j==i):
    print("Palindrome number")
else:
    print("Not a palindrome")