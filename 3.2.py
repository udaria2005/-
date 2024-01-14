s = input()
b = s.split()
for i in range(0, len(b)):
    j = int(b[i])
    if j%2 == 0:
        print(b[i], end=' ')