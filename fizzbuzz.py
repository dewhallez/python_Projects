#!/usr/bin/env python3

# Python fizzbuzz implementation

for num in range (1, 25):
    #check if number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        #check if number divisible by 3
    elif num % 3 == 0:
        print("Fizz")
        # check if number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    else:
        # return number not divisible by 3 or 5
        print(num)
