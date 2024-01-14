a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = -1
for x in range(0, 1001):
    if a*x**3 + b*x**2 + c*x + d == 0:
        k = x
        print(k) 
    else:
        k = k;
