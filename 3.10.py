s = input()
b = s.split()
for i in range(1, len(b), 2):
    j = b[i]
    l = b[i-1]
    b[i] = l
    b[i-1] = j
for m in range(0, len(b)):
    print(b[m], end=' ')
    
