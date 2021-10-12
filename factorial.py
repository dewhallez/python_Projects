#!/usr/bin/env python3
import math

print("Welcome to the Factorial CalculatorApp ")

# User input
number = int(input("What number would you like to calculate it's factorial: "))

print(str(number) + "! = ", end="")
for i in range(1, number):
    print(str(i), end="*")
print(str(number))

fact = math.factorial(number)
print("\nHere is the result with the built in math library factorial function")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

fact = 1
for i in range(1, number + 1):
    fact = fact * i
print("\nHere is the result with user built algorithm: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

