# Joseph Jones
# 9/24/2024
# P1HW1
# Get integer input from user and perform math calculations

# Display output to user
print("----Calculating Exponents----")
print()
print()

# Get info from user
base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calculate the value of the exponent math
result = base_value ** exponent

# Display results of the math
print(base_value, "raised to the power of", exponent, "is", result, "!!")
print()
print()

# Display output to user
print("----Addition and Subtraction----")
print()
print()

# Get info from user
start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate the value of the add and subtract math
math = start + add - subtract

# Display results of the math
print(start, "+", add, "-", subtract, "is equal to", math)
