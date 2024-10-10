# Joseph Jones
# 10/10/2024
# P2LAB2
# Using dictionaries

# Create a dictionary
cars ={"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Varible that holds only the keys from dictionary
keys =cars.keys()

# Show all keys to the user
print(keys)

# Get key from user
selected_car =input("Enter a vehicle to see it's mpg: ")
print()

# Display the selected car and the mpg
print(f"The {selected_car} gets {cars[selected_car]} mpg.")
print()

# Get the number of miles to drive the car
miles_planned =float(input(f"How many miles will you drive the {selected_car}? "))
print()

# Calculate gallons of gas needed
gas_needed =miles_planned / cars[selected_car]

# Display gallons needed to user
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {selected_car} {miles_planned} miles.")
