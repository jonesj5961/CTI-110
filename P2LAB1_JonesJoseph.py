# Joseph Jones
# 10/08/24
# P2LAB1
# Using Python's built-in math library

# Import math library
import math

print(f"The value of pi is {math.pi}\n")

# Get radius from user
radius =float(input("What is the radius of the circle? "))
print()

# Calculate the diameter
diameter =2 * radius

# Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate the circumference
circum =2 * math.pi * radius

# Display circumference with two decimal places
print(f"The circumference of the circle is {circum:.2f}\n")

# Calculate the area
area =math.pi * math.pow(radius, 2)

# Display area with three decimal places
print(f"The area of the circle is {area:.3f}")
