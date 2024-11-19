# Using functions in Python

# Define a function that adds numbers
def add_numbers(num1, num2, num3):
    result = num1 + num2 + num3
    print(f"{result}")



def main():
    # Main logic goes here
    print("The main is running...")
    # Call the add_numbers function
    add_numbers(3,5,1)
    add_numbers(0,0,0)
    add_numbers("egg","bacon","bread")


# Call the main function
if __name__ == "__main__":
    main()
