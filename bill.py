# Water Bill Calculation Program

# Get the number of units consumed from the user
units = int(input("Enter the number of water units consumed: "))

# Initialize bill amount
bill = 0

# Calculate the bill based on the given rate chart
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 8)
else:
    bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)

# Display the total bill
print(f"Total water bill: ₹{bill}") 