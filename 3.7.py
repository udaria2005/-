s = input()
b = s.split()
h = int(input())
k = 0
for i in range(0, len(b)):
    j = int(b[i])
    if h <= j:
        k = k+1
print(k+1)
    