a = 0
b = 0
c = 1

for i in range(15):
    a = b + c
    print(f' {b} + {c} = {a}')

    b = c
    c = a

    