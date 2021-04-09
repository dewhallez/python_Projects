#!/usr/bin/env python3

# Check if number is prime, return TRUE or FALSE

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5)+1 ):
        if num % i == 0: return False
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(15))
print(is_prime(21))
print(is_prime(32))
print(is_prime(51))