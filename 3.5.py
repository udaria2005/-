s = input()
b = s.split()
k = int(b[0])
l = 0
for i in range(0, len(b)):
    j = int(b[i])
    if j > k:
        k = j
        l = i
    else:
        k = k
        l = l
print(k,l)