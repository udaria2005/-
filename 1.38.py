n = int(input())
for i in range(1, n+1):
    f = (i)**(1/2)
    ff = round(f)
    if ff == f:
        print(i)