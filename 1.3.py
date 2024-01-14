a = int(input())
c = 0
b = 0
if ((a > -1000) and (a < 1000)):
    c = a + 1
    b = a - 1
    d = str(c)
    e = str(b)
    g = str(a)
    f = 'The next number for the number ' + g + ' is ' + d + '.'
    h = 'The previous number for the number ' + g + ' is ' + e + '.'
    print(f)
    print(h)
else:
    print('error, please try again')