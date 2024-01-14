s = input()
b = s.split()
k = 10000000
for i in range(0, len(b)):
    j = int(b[i])
    if j < k and j > 0:
        k = j
    else:
        k = k
print(k)