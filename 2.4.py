def IsPointInSquare(x, y):
    while abs(y+x) > 1 or abs(x-y) > 1:
        print('NO')
        break;
    while abs(y+x) <= 1 and abs(x-y) <= 1:
        print('YES')
        break;
    
a = float(input())
b = float(input())
IsPointInSquare(a, b)