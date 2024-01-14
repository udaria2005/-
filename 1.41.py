n = int(input())
s = 1
while s < n:
    if s < n:
        if s * 2 > n:
            break
        else:
            s = s * 2
            if s == n:
                print('YES')
if s != n:
    print('NO')
elif s == 1:
    print('YES')