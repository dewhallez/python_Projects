# code to calculate factorials of a given integer using recursion 

def fact(i):
    if i == 1:
        return 1
    else:
        return i * (i - 1)

print(fact(10))
print(fact(5))
