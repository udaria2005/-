def IsPointInSquare(x, y, xc, yc, r):
    xx = x - xc
    yy = y - yc
    rr = (xx**2 + yy**2)**0.5
    while rr > r:
        print('NO')
        break;
    while rr <= r:
        print('YES')
        break;
    
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
IsPointInSquare(a, b, c, d, e)