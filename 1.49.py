k = 0
p = 0
n = int(input())
while n != 0:
    if n >= p:
        k = p
        p = n
    if k < n and n < p:
        k = n
    n = int(input())
print(k)