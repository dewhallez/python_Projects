#!/usr/bin/env python3
from math import pi


# This program will calculate to a given number of digits using Pi function from the MAth Library.

Nplace = int(input("How many decimal places would you like to calculate: "))
# Set limit of decimal places program can calculate
while Nplace > 50:
    print("Number is too large")
    Nplace = int(input("Enter a number less than 50: "))
else:
    print(f'Pi to the {Nplace}th digit is {pi:{1}.{Nplace + 1}}')



# Sample outputs
# ➜  python_Projects git:(main) ✗ python3 Nth_valueofPi.py 
# How many decimal places would you like to calculate: 55
# Number is too large
# Enter a number less than 50: 12
# Pi to the 12th digit is 3.14159265359

# ➜  python_Projects git:(main) ✗ python3 Nth_valueofPi.py 
# How many decimal places would you like to calculate: 26
# Pi to the 26th digit is 3.14159265358979311599796347