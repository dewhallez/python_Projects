#!/usr/bin/env python3

#simple fibonacci nth digit calculator


#define function
def fibo(n):
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(15))



# To print a list of sequence to a given number
for i in range(20):
    print(i, fibo(i))



# Sample output
""" 
    ➜  python_Projects git:(main) ✗ python3 fibo.py
    610
    0 0
    1 1
    2 1
    3 2
    4 3
    5 5
    6 8
    7 13
    8 21
    9 34
    10 55
    11 89
    12 144
    13 233
    14 377
    15 610
    16 987
    17 1597
    18 2584
    19 4181

"""
