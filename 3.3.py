s = input()
b = s.split()
k = 0
for i in range(0, len(b)):
    j = int(b[i])
    if j > 0:
        k = k+1
print(k)