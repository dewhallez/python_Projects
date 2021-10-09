# Program to calculate right angle of a triangle
import math

print("Welcome to the Right Triangle Solver App.")

# Get input from user
first_side = float(input("What is the first leg of the Triangle: "))
second_side = float(input("What is the second leg of the triangle: "))

# Solve for right angle using pythagorean theorem
third_side = math.sqrt(first_side**2 + second_side**2)
third_side = round(third_side, 2)

# Calculate Area
area = 0.5 * first_side * second_side
area = round(area, 2)

# Display result

print("\nFor a triangle with legs of " + str(first_side) + " and " + str(second_side) + " the hypotenuse is " + str(third_side) + ".")
print("For a triangle with legs of " + str(first_side) + " and " + str(second_side) + " the Area is " + str(area) + ".")
