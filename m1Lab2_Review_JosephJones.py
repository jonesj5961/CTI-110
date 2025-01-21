# Joseph Jones
# 1/21/2025
# CSC121 m1Lab2
# This program determines the fastest route based on user input.

'''
1. Initialize variables to keep track of the fastest route and its time.
2. Create a loop to accept route data from the user.
a. Prompt for the distance (miles) and validate it.
b. Prompt for the speed (miles/hour) and validate it.
c. Calculate the travel time in minutes (distance/speed * 60).
d. Display the travel time.
e. Update the fastest route if the current one is faster.
f. Ask if the user wants to enter more routes.
3. After the loop, display the fastest route and its travel time. 
'''

# Initialize variables
fastest_route = None
fastest_time = float('inf') # Set to a very large number
route_number = 1 # Route counter

while True:
    try:
        # Input for distance
        distance = float(input(f"Enter route {route_number} distance (miles): "))
        while distance <= 0:
            print("Distance must be greater than 0.")
            distance = float(input(f"Enter route {route_number} distance (miles): "))

        # Input for speed
        speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
        while speed <= 0:
            print("Speed must be greater than 0.")
            speed = float(input(f"Enter route {route_number} speed (miles/hour): "))

        # Calculate time in minutes
        time = (distance / speed) * 60
        print(f"Route {route_number} time: {time:.2f} minutes")

        # Update fastest route if applicable
        if time < fastest_time:
            fastest_time = time
            fastest_route = route_number

        # Ask if more routes are to be entered
        more_routes = input("More routes (y/n)?: ").strip().lower()
        while more_routes not in ('y', 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            more_routes = input("More routes (y/n)?: ").strip().lower()

        if more_routes == 'n':
            break

        route_number += 1

    except ValueError:
        print("Invalid input. Please enter numeric values for distance and speed.")

# Display the fastest route
if fastest_route is not None:
    print(f"Route {fastest_route} is fastest; {fastest_time:.2f} minutes")
else:
    print("No routes were entered.")