#!/usr/bin/env python3

# if/else conditions

print("Welcome to the Shipping Account Program")
users = ['john', 'mike', 'jane', 'david', 'ayo', 'akin']

# User input
username = input("\nPlease enter your username: ").lower().strip()

# Check if user is in the list of users
if username in users:
    # print price summary
    print("\nHello " + username + ". Welcome back!")
    print("Here are the currently shipping prices:")
    print("Shipping orders 0 to 100: \t\t$5.10 each")
    print("Shipping orders 100 to 500: \t\t$5.00 each")
    print("Shipping orders 500 to 1000: \t\t$4.95 each")
    print("Shipping orders over 1000: \t\t$4.80 each")


# Calculate price based in items to be shipped
    quantity = int(input("\nHow many items would you like to ship today: "))
    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80

    # Display final cost
    bill = quantity * cost
    bill = round(bill, 2)
    print("To ship " + str(quantity) + " items it will cost you $" + str(bill) + " at $" + str(cost) + " per item.")

    # Order placement
    choice = input("\nWould you like to proceed with this order (y/n): ").lower()
    if choice.startswith('y'):
        print("Okay, Shipping your " + str(quantity) + " items.")
    else:
        print("Okay. No orders will be placed at this time")

# User not in the registered list
else:
    print("Sorry, you have to be a registered user to place orders.")

