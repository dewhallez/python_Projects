#!/usr/bin/env python3

import random

print("Welcome to the number guessing game")
name = input("Hello! What is your name: ").title().strip()

# Pick a random number
print("Well " + name + ", I am thinking of a random number between 1 and 20.")
number = random.randint(1, 20)

# Guesses with 5 tries

for guess_num in range(5):
    guess = int(input("\nTake a guess: "))

    if guess < number:
        print("Your guess is too low!")
    elif guess > number:
        print("Your guess is too high!")
    else:
        break

# Game is done
if guess == number:
    print("\nGood job, " + name + "! You guessed my number in " + str(guess_num + 1) + " guesses")
else:
    print("\nGame over. The number I was thinking of was " + str(number) + ".")

