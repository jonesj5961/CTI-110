import random
'''
Create a class called car with the following attributes:
Make
Model
Color
Driver
max_speed_in miles (a value between 10 and 80)
handling(a value between 1 and 12)
It should also have the following methods:
accelerates
breaks_down()
crash(handling)
turbo_boost()
Then write a program that lets the user begin a race with at least two cars
Simulate a race using the instances of the Car class and associated methods
'''

class Car:
    # Define the class function that initializes (or creates the objects)
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make
        self.model = model
        self.color = color
        self.driver = driver
        self.max_speed = max_speed
        self.handling = handling
        self.miles_driven = 0

    # Create an instance method that works on any object of the class Car
    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver}")

    def drive_car(self):
        self.miles_driven += random.randint(5, self.max_speed) + self.handling
    
    def show_stats(self, miles_to_win):
        print(f"{self.driver}'s car advanced to {self.miles_driven}")
        print()
        if self.miles_driven >= miles_to_win:  # Changed to >= to ensure the win is caught
            print(f"{self.driver} won the race!!!")
            return True  # Indicate that someone won
        return False

    def hit_maxwell(self):
        hit = random.randint(1, 3)
        if hit == 1:
            print(f"💥💥💥🙀💥💥💥 Maxwell was hit by {self.driver}!")
            reduce_speed = random.randint(10, 20)
            self.max_speed -= reduce_speed
            print(f"{self.driver}'s max speed was reduced by {reduce_speed}!")
            print()
        else:
            print(f"Maxwell managed to save himself from {self.driver}!👌😸")

def main():
    miles_to_win = 100
    # Create a car object
    muskCar = Car("Mazda", "Miata", "orange", "Elon Musk", 60, 11)
    # Create a second car
    bezosCar = Car("Nissan", "Sentra", "silver", "Jeff Bezos", 50, 12)

    print("The race is beginning.....")
    print("🏁🏁🏁🏁🏁")

    # Call the instance function show_car_info
    muskCar.show_car_info()
    print()
    bezosCar.show_car_info()

    while muskCar.miles_driven < 100 and bezosCar.miles_driven < 100:
        # Drive both cars one time
        muskCar.drive_car()
        bezosCar.drive_car()

        print()
        # Show the updated status of the car
        if muskCar.show_stats(miles_to_win) or bezosCar.show_stats(miles_to_win):
            break  # Exit the loop if there's a winner

        # Call the hit_maxwell method on both Car objects
        muskCar.hit_maxwell()
        print()
        bezosCar.hit_maxwell()

if __name__ == "__main__":
    main()
        bezosCar.hit_maxwell()

if __name__ == "__main__":
    main()
