s = input()
b = s.split()
for i in range(1, len(b)):
    j = int(b[i])
    l = int(b[i-1])
    if (j >= 0 and l >= 0) or (j < 0 and l < 0):
        print(b[i-1],b[i]);
        break