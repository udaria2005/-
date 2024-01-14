a = int(input())
b = int(input())
l = int(input())
N = int(input())
x = 0
for i in range(1, N):
    x = x + a + b
x = x + a + l
y = x*2 - a
print(y)