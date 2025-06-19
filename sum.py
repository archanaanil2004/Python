num = int(input("Enter a number: "))
sum  = 0
temp = num

while temp > 0:
    digit = temp % 10      # Get the last digit
    sum += digit    # Add it to sum
    temp //= 10 
print("the sum=",sum)     