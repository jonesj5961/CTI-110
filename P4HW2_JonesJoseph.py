# Joseph Jones
# 11/14/2024
# P4HW2
# Calculate pay based on overtime and regular hours for multiple employees.

# Initialize totals
total_employees =0
total_overtime_pay =0.0
total_regular_pay =0.0
total_gross_pay =0.0

# Variable to control the loop
name =input("Enter employee's name or 'Done' to terminate: ")

# Loop to calculate pay for each employee until "Done" is entered
while name.lower() != "done":
    # Input: Get hours worked from user (float hours)
    hours =float(input(f"Enter number of hours {name} worked: "))
    # Input: Get pay rate from user (float pay_rate)
    pay_rate =float(input(f"Enter {name}'s pay rate: "))
    # Print: dotted line and employee's name
    print()
    print("=" * 40)
    print(f"Employee Name: {name}")
    # Calculate pay
    if hours > 40:
        ot_hours =hours - 40
        ot_pay_rate =pay_rate * 1.5
        ot_pay =ot_hours * ot_pay_rate
        regular_pay =40 * pay_rate
        gross_pay =regular_pay + ot_pay
    else:
        ot_hours =0
        ot_pay =0
        regular_pay =hours * pay_rate
        gross_pay =regular_pay
    # Display individual employee results
    print()
    print(f"{'Hours Worked':<13}{'Pay Rate':<13}{'Overtime':<13}{'Overtime Pay':<13}{'Regular Pay':<13}{'Gross Pay':<13}")
    print(f"{hours:<13.1f}{pay_rate:<13.2f}{ot_hours:<13.1f}{ot_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<13.2f}")
    print("=" * 40)
    # Update totals
    total_employees += 1
    total_overtime_pay += ot_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    print()
    name =input("Enter employee's name or 'Done' to terminate: ")

# Display totals for all employees after loop ends
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
