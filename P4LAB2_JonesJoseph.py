# Joseph Jones
# 11/7/2024
# P4LAB2
# Use loops to show only postive times tables

run_again ="yes"

while run_again.lower() !="no":
    # Get integer from user
    user_num = int(input("Enter an integer: "))
    # If integer is zero or higher, show times table
    if user_num >= 0:
        for item in range(1, 13):
    # Use a loop to show times table
            print(f"{user_num} * {item} = {user_num * item}")
    # If integer is negative, tell user no can do
    else:
        print("This program does not handle negative values")
    
    run_again =input("Would you like to run the program again? ")
print("Progam has ended")
