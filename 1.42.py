n = int(input())
s = 1
k = 0
while s < n:
    if s < n:
        if s * 2 >= n:
            break
        else:
            s = s * 2
            k = k + 1
if n > 1:
    k = k + 1
    print(k)
else:
    print(k)