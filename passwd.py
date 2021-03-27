#!//use/bin/env python3


#Simple python code to generate random password with user generated length.

import random 
import string

#concancating imported strings for password
password_characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits

#Starting with a blank password
password = []

#Get user input for length of password

password_length = int(input("Enter the length of desired password: "))

#loop strings to generate random password

for char in range(password_length):
    password.append(random.choice(password_characters))

#print out generated password
print("".join (password))


