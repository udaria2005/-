a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (abs(c-a)+abs(d-b))%2 == 0:
    print('YES')
else:
    print('NO')