# Joseph Jones
# 10/29/2024
# P3HW2
# Program calculates pay based on OT or no OT

'''
Input: Get employee name from user - string (name)
Input: Get hours worked from user - int (hours)
Input: Get pay rate from user - float (pay_rate)

Output: print dotted line and employee name

If hours is greater than 40 (employee has OT)
    variable for hours worked already exists (don't have to recreate)
    (don't have to create pay rate, it already exists)
    create a variable (OT) that holds only the OT hours (hours - 40)
    create a variable for OT_pay_rate (pay_rate * 1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay (pay_rate * 40)
    calculate gross pay (pay for OT + regular pay)
else (NO OT - hours has to be 40 or less)
    create a variable (OT) that holds only the OT hours WHICH IS ZERO
    calculate pay for OT hours WHICH IS ZERO
    calculate regular pay (pay_rate * hours)
    calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print("{'Hours Worked':<20}{'Pay Rate':<20}")
print(f"{hours:<20}${pay_rate:<20.2f}")

'''

# Enter values from user
name =input("Enter employee's name: ")
hours =int(input("Enter number of hours worked: "))
pay_rate =float(input("Enter employee's pay rate: "))

# Print a dotted line and employees's name
print("-" * 40)
print(f"Employee Name:  {name}")

# Calculate pay
if hours > 40:
    ot_hours =hours - 40
    ot_pay_rate =pay_rate * 1.5
    ot_pay =ot_hours * ot_pay_rate
    regular_pay =pay_rate * 40
    gross_pay =regular_pay + ot_pay
else:
    ot_hours =0
    ot_pay =0
    regular_pay =pay_rate * hours
    gross_pay =regular_pay

# Display results
print()
print(f"{'Hours Worked':<13}{'Pay Rate':<13}{'OverTime':<13}{'OverTime Pay':<13}{'RegHour Pay':<13}{'Gross Pay':<13}")
print("--" * 40)
print(f"{hours:<13.1f}{pay_rate:<13.1f}{ot_hours:<13.1f}{ot_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<13.2f}")
