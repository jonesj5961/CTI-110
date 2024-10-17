# Joseph Jones
# 10/17/2024
# P2HW1
# Create a program that does some basic math on numbers that are entered.
# And change how results are displayed

# Display output to user
print("This program calculates and displays travel expenses")
print()

# Enter user budget
budget = int(input("Enter Budget: "))
print()

# Enter user destination
destination = input("Enter your travel destination: ")
print()

# Enter user gas purchases
fuel = int(input("How much do you think you will spend on gas? "))
print()

# Enter user accomodations
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# Enter user food
food = int(input("Last, how much do you need for food? "))
print()

# Display travel expenses to user
print("------------Travel Expenses------------")
print(f"{'Location: ':<19}{destination}")
print(f"{'Initial Budget: ':<19}${budget:,.2f}")
print(f"{'Fuel: ':<19}${fuel:,.2f}")
print(f"{'Accomodation: ':<19}${accomodation:,.2f}")
print(f"{'Food: ':<19}${food:,.2f}")
print("-" * 39)
print()

# Add expenses
add = fuel + accomodation + food

# Subtract expenses
subtract = budget - add

# Display results
print(f"{'Remaining Balance: ':<19}${subtract:,.2f}")
