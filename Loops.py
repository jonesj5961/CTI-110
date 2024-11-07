# For loop using the range function with one parameter

'''
for var in range(5):
    print(var+1)
    #print("Apples are delicious!")
'''

'''
# For loop using the range function with two parameters
# Parameters are starting value and stop value, stop is not inclusive
end_num =14

for item in range(7,end_num+1):
    print(item)
'''

'''
# For loop using the range function with three parameters
# Parameters are start, stop (not inclusive), number to increase by

for cat in range(0,101,5):
    print(cat)
'''

# Loop through listand print each item
myList =["one", 2, 2.5, "three", 4, 4.5, "five", False]

for thing in myList:
    print(thing)

numList =[10, 20, 30, 40, 50]

total =0
for num in numList:
    total = total + num
print(f"The final total is {total}")
