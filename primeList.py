#!/usr/bin/env python3

def primeList(number):   
    # initialize a list to hold numbers
    primeNumbers = []
    # check for prime number in range provided
    for primes in range(2, number + 1):        
        is_number_Prime = True

        for num in range(2, int(primes ** 0.5) + 1):
            # check for non-prime numbers
            if primes % num == 0:
                is_number_Prime = False  
                break     
            
              
        if is_number_Prime:
            primeNumbers.append(primes)
    return(primeNumbers)

print(primeList(101))


# sample output
# ➜  python_Projects git:(main) ✗ python3 primeList.py 
#  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]