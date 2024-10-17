# In-class examples using lists

'''
# Create an empty list
myfam =[]

# Add values to the list
myfam.append("Joseph")
myfam.append("Jordyn")
myfam.append("John")
myfam.append("Jamie")

# Display list
print(myfam)

# Print item at index 3
print(myfam[3])

# Print items from index 1 to 3 (goes up to but not including 3)
# Add one to your ending index
print(myfam[1:4])

# Remove item from list by its value
myfam.remove("Joseph")

print(f"\n\n Remove Joseph....")
print(myfam)

# Remove item from list by its index
myfam.pop(1)

print(f"\n\n Remove Jordyn....")
print(myfam)
'''

num1 =int(input("gimme a number: "))
num2 =int(input("gimme a number: "))
num3 =int(input("gimme a number: "))
num4 =int(input("gimme a number: "))

# Create the list with the values in it
numbers =[num1, num2, num3, num4]

print(numbers)

# Functions that use lists

# Gives back the number of items in the list
print(f"There are {len(numbers)} items in the list.")

# Get the highest value in list
print(f"The highest value in the list is {max(numbers)}")

# Get the lowest value in list
print(f"The lowest value in the list is {min(numbers)}")

# Get the sum of all values in the list
print(f"The sum of values in the list is {sum(numbers)}")

# Get the average
average= sum(numbers)/len(numbers)

# Display average
print(f"The average of the values in the list is {average}")
