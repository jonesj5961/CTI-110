# Joseph Jones
# 11/12/2024
# PA4HW
# Calculate and display user's grades

# Ask user for the number of scores they would like to enter
num_scores = int(input("How many scores do you want to enter? "))

# Empty list to store valid scores
scores = []

# Loop to get the scores
for i in range(num_scores):
    while True:
        score = int(input(f"Enter score #{i + 1}: "))

        # Ensure score is between 0 and 100
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i + 1} again:")

# Calculate results
lowest_score = min(scores)
modified_scores = [s for s in scores if s != lowest_score]  # Drop lowest score
average_score = sum(modified_scores) / len(modified_scores)

# Determine letter grade for the average score
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display the results
print("\n------------Results------------")
print("Lowest Score:", f"{lowest_score:.1f}")
print("Modified List:", ["{:.1f}".format(x) for x in modified_scores])
print("Scores Average:", f"{average_score:.2f}")
print("Grade:", grade)
print("-------------------------------")
