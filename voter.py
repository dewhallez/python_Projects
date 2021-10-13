#!/usr/bin/env python3

print("Welcome to the Voter Registration App")

# Get user input

name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

# List of parties

parties = ['Democratic', 'Republican', 'Independent', 'Libertarian', 'Green']

# Verify user age

if age > 17:
    print("\nCongratulations " + name + "! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")

    # Display list of parties
    for party in parties:
        print("\t- " + party)

    # Get user input for party to join
    chosen_party = input("\nWhat party would you like to join: ").title().strip()

    if chosen_party in parties:
        print("\nCongratulations " + name + "! You have joined the " + chosen_party + " party!")
        if chosen_party == "Republican" or chosen_party == "Democratic":
            print("That is a major party!")
        elif chosen_party == "Independent":
            print("You are an Independent person")
        else:
            print("That is not a major party.")
    else:
        print("That is not a valid party option.")


# if user is younger than 18
else:
    print("\nYou are not old enough to vote, come back when you are at least 18 years old.")