# Welcome Message

print("Welcome to the Grade Sorter App")

# Initialize the grade list and get input
grades = []
grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

# Display list of grades
print("\nYour grades are: " + str(grades))

# Sort list from highest to lowest
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

# Remove the two lowest grades
print("\nDropping the two lowest grades.........")
removed = []
removed_grades = grades.pop()
removed.append(removed_grades)
#print("This grade will be removed: " + str(removed_grades))
removed_grades = grades.pop()
removed.append(removed_grades)
#print("This grade will be removed: " + str(removed_grades))
print("\nThese grades were removed: " + str(removed))

# Display remaining the grades
print("\nYour remaining grades are: " + str(grades))
print("Great Job! Your highest grade is " + str(grades[0]) + "!")

