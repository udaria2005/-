n = int(input())
s = 0
for i in range (2, n+1):
    s = s + i*(i-1)
b = str(s)
ss = ''
for a in range (2, n):
    e = a - 1;
    ss = ss + str(e) + '*' + str(a) + '+'
f = n - 1
ss = ss + str(f) + '*' + str(n) + '=' + b
print(ss)
    