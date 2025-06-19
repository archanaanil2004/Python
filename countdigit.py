num = int(input("Enter a number: "))
target_digit = int(input("Enter the digit to count: "))
count = 0
temp = num

while temp > 0:
    digit = temp % 10
    if digit == target_digit:
        count += 1
    temp //= 10

print(f"The digit {target_digit} appears {count} times.")