def IsPointInSquare(x, y):
    xx = x + 1
    yy = y - 1
    rr = (xx**2 + yy**2)**0.5
    while (rr >= 2 and y <= -x and y <= 2*x + 2) or (rr <= 2 and y >= 2*x + 2 and y >= -x):
        print('YES')
        break;
    while (rr > 2 and (y > -x or y > 2*x + 2)) or (rr < 2 and (y < -x or y < 2*x + 2) or (rr == 2 and ((y > -x and y < 2*x + 2) or (y < -x and y > 2*x + 2)))):
        print('NO')
        break;
    
a = float(input())
b = float(input())

IsPointInSquare(a, b)