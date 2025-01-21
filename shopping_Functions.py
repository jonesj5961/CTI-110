# Joseph Jones
# 1/16/2025
# M2Lab
# Use functions to simulate shopping

# Create the function to determine if the item exists
def if_item_exists(item):
    '''
    Function takes in one string.
    If that string exists in a list, return True, if the string not in list, return False.
    '''
    store_items = ["catnip", "collar", "cat sweater", "friskies", "brush"]

    if item in store_items:
        return True
    else:
        return False

def getCost(item, quantity):
    '''
    Function takes in an item as a string and a quantity as integer.
    Function calculate the cost using a dictionary and return the total cost.
    '''
    item_prices = {"catnip":99.99, "collar":7.89, "cat sweater":19.50, "friskies":0.89, "brush":5.00}

    # Get the cost of the item from the dictionary
    item_cost = item_prices[item]

    total_cost = item_cost * quantity

    return total_cost




# Define the main function
def main():
    # Call all our other functions
    print("Welcome to Cat-Co!!!")

    run_again = "yes"

    final_cost = 0

    while run_again == "yes":
        
        # Get an item from the user
        user_item = input("What do you want to purchase? ")

        if if_item_exists(user_item) == True:
            quantity = int(input(f"How many {user_item}s will you buy? "))
            final_cost = final_cost + getCost(user_item, quantity)
        else:
            print("That item does not exist!")

        run_again = input("Will you add more items? ")

    print(f"${final_cost:.2f}")
        
# Call the main
if __name__ == "__main__":
    main()
