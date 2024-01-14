s = input()
b = s.split()
k = 1
for i in range(0, len(b)-1):
    j = int(b[i])
    l = int(b[i+1])
    if j != l:
        k = k+1
print(k)