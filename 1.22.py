a = int(input())
b = int(input())
c = int(input())

n = 0
if a == b:
    n = n+1
else:
    n = n
if b == c:
    n = n+1
else:
    n = n
if c == a:
    n = n+1
else:
    n = n
if n == 0:
    n = 0
elif n == 1:
    n = 2
else:
    n = 3
print(n)