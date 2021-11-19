#! /usr/bin/env python3

""" Sample password hashing with bcrypt"""

import bcrypt

password = "KansasIsGoingByeBye23!"

def hashed_password(password: str) -> bytes:
    """ function takes a string argument"""
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


print(hashed_password(password))


# sample output
# b'$2b$12$1EXkw76rtZWTn4lLCUY3ueepBEy4AB1OHVvW0NCGqLQDxm.J1KOoC'