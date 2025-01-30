
############### NESTED DICTIONARY

animals = {
    "Big Cats": {
        "Lion": ["Asiatic Lion", "West African Lion", "South African Lion"],
        "Tiger": ["Bengal Tiger", "Siberian Tiger", "Indochinese Tiger"],
        "Cheetah": ["African Cheetah", "Asiatic Cheetah", "Saharan Cheetah"]
    },
    "Wild Dogs": {
        "Wolf": ["Arctic Wolf", "Gray Wolf", "Timber Wolf"],
        "Fox": ["Red Fox", "Silver Fox", "Cross Fox"],
        "Wild Dog": ["African Wild Dog", "Painted Wolf", "Cape Hunting Dog"]
    },
    "Bears": {
        "Brown Bear": ["Grizzly Bear", "Kodiak Bear", "Eurasian Brown Bear"],
        "Polar Bear": ["Greenland Polar Bear", "Hudson Bay Polar Bear"],
        "Andean Bear": ["Northern Andean Bear", "Southern Andean Bear"]
    }
}

# Describe the structure of the variable animals
'''
animals is a dictionary and each item in animals is also a dictionary where the
key is "Big Cats" and the value is another dictionary. Now the keys are Lion,
Tiger, and Cheetah and their values are lists
'''

# Pull specified data from the dictionary
# Print the list ["Red Fox", "Silver Fox", "Cross Fox"]
print(animals["Wild Dogs"]["Fox"])

# Retrieve the string "Silver Fox"
print(animals["Wild Dogs"]["Fox"][1])

# Retrieve the string "Greenland Polar Bear"
print(f"One type of Polar bear is the {animals['Bears']['Polar Bear'][0]}")

# Write a loop to display every piece of data in animals

print("\n\n\n\n")


# Loop through the nested dictionary

for a in animals: # animals is the outer dictionary
    print(a)
    for n in animals[a]: #animals[a] is the inner dictionary
        print("\t",n)
        #print("\t\t",animals[a][n]) #animals[a][n] is a list
        for i in animals[a][n]:
            print("\t\t",i)

'''
for key, value in animals.items():
    print(f"{key}{value}")
'''

################## THREE LEVEL NESTED LIST

'''
How the nesting works:
First level: Broad fish categories (Freshwater Fish, Saltwater Fish, Coral Reef Fish).
Second level: Types of fish within each category (e.g., Bass, Trout, Catfish).
Third level: Specific species of each type.
'''

fish_types = [
    ["Freshwater Fish", 
        ["Bass", 
            ["Largemouth Bass", "Smallmouth Bass", "Spotted Bass"]
        ],
        ["Trout", 
            ["Rainbow Trout", "Brown Trout", "Brook Trout"]
        ],
        ["Catfish", 
            ["Channel Catfish", "Blue Catfish", "Flathead Catfish"]
        ]
    ],
    ["Saltwater Fish", 
        ["Sharks", 
            ["Great White Shark", "Hammerhead Shark", "Tiger Shark"]
        ],
        ["Tuna", 
            ["Bluefin Tuna", "Yellowfin Tuna", "Albacore Tuna"]
        ],
        ["Marlin", 
            ["Blue Marlin", "White Marlin", "Black Marlin"]
        ]
    ],
    ["Coral Reef Fish", 
        ["Clownfish", 
            ["Common Clownfish", "Saddleback Clownfish", "Clark's Clownfish"]
        ],
        ["Angelfish", 
            ["Emperor Angelfish", "French Angelfish", "Queen Angelfish"]
        ],
        ["Parrotfish", 
            ["Stoplight Parrotfish", "Rainbow Parrotfish", "Bicolor Parrotfish"]
        ]
    ]
]
print("\n\n\n\n\n\n")
# Retrieve Queen Angelfish from fish_types
print(fish_types[2][2][1][2])


# Use some looping for each data structure
# Show each Broad fish categories (Freshwater Fish, Saltwater Fish, Coral Reef Fish).
# Then show each type of fish within that category
# Then show each species of fish within the category (most inner nested list)


######## NESTED DICTIONARY SIMILAR TO HOMEWORK

dog_breeds = {
    "Labrador Retriever": {
        "desc": "Friendly and outgoing, great family dog",
        "weight": 65,
        "cost": 800
    },
    "German Shepherd": {
        "desc": "Intelligent and versatile, often used in police work",
        "weight": 75,
        "cost": 1000
    },
    "Golden Retriever": {
        "desc": "Loyal and loving, excellent for therapy and assistance",
        "weight": 70,
        "cost": 900
    },
    "Bulldog": {
        "desc": "Gentle and affectionate, known for their wrinkled face",
        "weight": 50,
        "cost": 1200
    },
    "Poodle": {
        "desc": "Highly intelligent and hypoallergenic coat",
        "weight": 45,
        "cost": 1500
    }
}
print("\n\n\n\n\n\n")
# Let's pull some info from the dictinary and loop through it :)
# Retrieve cost of Bulldog
print(dog_breeds["Bulldog"]["cost"])
print("\n\n\n\n")

# Loop through dog_breeds
for key in dog_breeds:
    print(key)
    for inner_key in dog_breeds[key]: # dog_breeds[key] is a dictionary
        print("\t", inner_key, ":", dog_breeds[key][inner_key])
    
