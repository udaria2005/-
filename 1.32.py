from math import factorial
n = int(input())
k = int(input())
a = factorial(n)
b = factorial(k)
c = factorial(n-k)

h = a/(b*c)
coolh = int(h)
print(coolh)