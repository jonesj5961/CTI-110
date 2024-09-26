# Joseph Jones
# 9/26/2024
# P1HW2
# Create a program that does some basic math on numbers that are entered.

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
print("----Travel Expenses----")
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", fuel)
print("Accomodation: ", accomodation)
print("Food: ", food)
print()

# Add expenses
add = fuel + accomodation + food

# Subtract expenses
subtract = budget - add

# Display results
print("Remaining Balance: ", subtract)
