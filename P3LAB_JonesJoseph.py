# Joseph Jones
# 10/29/2024
# P3LAB
# Using integer division and if/else statements

# Get float from user
money =float(input("Enter the amount of money as a float: $"))

print(f"Change Amount: {money}")

# Convert float value into an integer
money =round(money * 100)

print(f"Change Amount: {money}")

if money == 0:
    print("No Change Due")

# Calculate the amount of each coin needed
#integer division - //

num_dollars = money // 100
money = money - (num_dollars * 100)

num_quarters = money // 25
money = money - (num_quarters * 25)

num_dimes = money // 10
money = money - (num_dimes * 10)

num_nickels = money // 5
money = money - (num_nickels * 5)

num_pennies = money


# Display coins owed

if num_dollars > 0:
    if num_dollars == 1:
        print(num_dollars, "Dollar")
    else:
        print(num_dollars, "Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(num_quarters, "Quarter")
    else:
        print(num_quarters, "Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(num_dimes, "Dimes")
    else:
        print(num_dimes, "Dimes")

if num_nickels > 0:
    if num_dollars == 1:
        print(num_nickels, "Nickel")
    else:
        print(num_nickels, "Nickels")

if num_pennies > 0:
    if num_dollars == 1:
        print(num_pennies, "Penny")
    else:
        print(num_pennies, "Pennies")
