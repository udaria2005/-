from math import pow
def power(a,n):
    c = pow(a,n)
    if c - int(c) != 0:
        print(c)
    else:
        print(int(c))
x = float(input())
y = int(input())
power(x,y)