def IsPointInSquare(x, y):
    while abs(x) > 1 or abs(y) > 1:
        print('NO')
        break;
    while abs(x) <= 1 and abs(y) <= 1:
        print('YES')
        break;
    
a = float(input())
b = float(input())
IsPointInSquare(a, b)