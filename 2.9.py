import math
def reduce_fraction(n,m):
    k = math.gcd(n,m)
    print(n//k, m//k)
a = int(input())
b = int(input())
reduce_fraction(a,b)