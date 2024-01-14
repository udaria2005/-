k = 0
p = 0
n = 1
while n != 0:
    n = int(input())
    if n > p:
        k = k+1
        p = n
    else:
        k = k
        p = n
if k == 0:
    print(k)
else:
    print(k-1)

