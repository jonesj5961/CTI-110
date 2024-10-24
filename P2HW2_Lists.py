

# Request grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# create list and add grades to list

gradeList = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]


# determine, lowest, highest, sum and average

lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
avg = sum(gradeList)/len(gradeList)

# display results

print("\n------------Results------------")
print(f'{"Lowest Grade:":<20}{lowest}')
print(f'{"Highest Grade:":<20}{highest}')
print(f'{"Sum of Grades:":<20}{total}')
print(f'{"Average:":<20}{avg:.2f}')

print("----------------------------------------")





