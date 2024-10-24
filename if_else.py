# if/else statements

num1 =1
num2 =1

'''
if num1 == num2:
    print(f"{num1} is equal to {num2}")

elif num1 > num2:
    print(f"{num1} is greater than {num2}")

else:
    print(f"{num1} is NOT greater than {num2}")
'''

'''
# Get input from user
age =int(input("Enter an age: "))

if age > 65:
    life_stage ="Senior"
elif age > 17:
    life_stage ="Adult"
elif age > 12:
    life_stage ="Teenager"
elif age > 5:
    life_stage ="Child"
elif age > 0:
    life_stage="Baby/Toddler"

print(f"You are {age} years old and you are a {life_stage}")
'''

age =int(input("Enter an age: "))

if age >= 0 and age <= 5:
    life_stage ="Baby/Toddler"
if age >= 6 and age <= 12:
    life_stage ="Child"
if age >= 13 and age <= 17:
    life_stage ="Teenager"
if age >= 18 and age <= 65:
    life_stage ="Adult"
if age >= 66:
    life_stage ="Senior"

print(f"You are {age} years old and you are a {life_stage}")
