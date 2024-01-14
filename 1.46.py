k = 0
p = 0
n = 1
while n != 0:
    n = int(input())
    k = k+n
    p = p+1
if p > 1:
    s = (k)/(p-1)
    print(s)
else:
    print(k)