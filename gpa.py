#!/usr/bin/env python3

# Welcome message and get user name
print("Hello and welcome to the Grade Point Average Calculator App")
name = input("What is your name: ").title().strip()
grade_num = int(input("How many grades do you like to enter: "))

# Get grades from user
grades = []

for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

grades.sort(reverse=True)
print("\nGrades Highest to Lowest:")
for grade in grades:
    print("\t" + str(grade))

# Average grade calculation
average = sum(grades) / len(grades)
average = round(average, 2)

# Print average grade
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average))

# get desired average from user and calculate what grade to get this average
desired_average = float(input("\nWhat is your desired average: "))
grade_needed = desired_average * (len(grades) + 1) - sum(grades)
desired_average = round(grade_needed, 2)

# Print Summary
print("\nGood Luck " + name + "!")
print("You will need to get a " + str(grade_needed) + " on your next test to earn a " + str(desired_average))

# Swap out one of the original grades
new_grades = grades[:]
print("\nLets see what your average could have been if you did better/worse on a text.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = int(input("What grade would you like to change " + str(grade_change) + " to: "))
new_grades.append(new_grade)

# Sort the new grades
new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest: ")
for grade in new_grades:
    print("\t" + str(grade))


# New Average grade calculation
new_average = sum(new_grades) / len(new_grades)
new_average = round(new_average, 2)

# Print new average grade
print("\n" + name + "'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(new_grades)))
print("\tHighest Grade: " + str(max(new_grades)))
print("\tLowest Grade: " + str(min(new_grades)))
print("\tAverage: " + str(new_average))

# Summary of change in average grade
print("\nYour new average would be a " + str(new_average) + " compared to your real average of " + str(average))
average_change = new_average - average
average_change = round(average_change, 2)
print("That is a change of " + str(average_change) + " points!")

print("\nYou original grades are unchanged!")
print(grades)
print("You should ask for extra credit opportunities!")

