# Joseph Jones
# 3/13/2025
# M3Lab1
# Reading csv data into class objects

import csv

# Make a class
class Customer:
    # Create __init__ function
    def __init__(self, first, last, phone, email, state, address):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.state = state
        self.address = address

    def display_info(self):
        return f"\n\n{self.first} {self.last}\n{self.phone}\n{self.email}\n{self.address}, {self.state}\n\n"
'''    
# Test
customer1 = Customer("Janice", "Miller", "704-555-4521", "jayjay@aol.com", "NC", "255 Hull Rd.")
print(customer1.display_info())'
'''
# Create empty list to hold csv info
customer_input = []
with open('customer.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        customer_input.append(row)
    
print(customer_input)



# TO DO:
'''
Reiterate through the nested list. Ignore the first inner list.
FOr each remaining list 
'''