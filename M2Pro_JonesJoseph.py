# Joseph Jones
# 1/21/2025
# M2Pro
# The program should allow the user to calcuate the cost a customer is to pay depending on the following: Number of items, Each item in the store cost $1, Customers who buy 10 or more items are to get a 5% discount, 6.2% sales tax is applied on cost



# Function to calculate the discount
def calculate_discount(cost, items):
    """Applies a 5% discount for 10 or more items."""
    if items >= 10:
        discount = cost * 0.05
        return cost - discount
    return cost

# Function to calculate sales tax
def calculate_sales_tax(cost):
    """Applies a 6.2% sales tax to the cost."""
    sales_tax_rate = 0.062
    return cost * sales_tax_rate

# Function to calculate total cost
def calculate_total_cost(items):
    """Calculates the total cost based on the number of items."""
    item_cost = 1  # Each item costs $1
    cost = items * item_cost  # Total cost before discount and tax
    cost_after_discount = calculate_discount(cost, items)
    sales_tax = calculate_sales_tax(cost_after_discount)
    total_cost = cost_after_discount + sales_tax
    return total_cost

# Function to display the menu and handle user input
def display_menu():
    """Displays the menu and processes user input."""
    while True:
        print("\n==== Welcome to the Store ====")
        print("1. Calculate Total Cost")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            try:
                items = int(input("Enter the number of items: "))
                if items < 0:
                    print("Number of items cannot be negative. Please try again.")
                else:
                    total_cost = calculate_total_cost(items)
                    print(f"Total cost for {items} items is: ${total_cost:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

# Main function to run the program
if __name__ == "__main__":
    display_menu()
