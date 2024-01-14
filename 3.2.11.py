n = int(input())
s = []
for i in range(n):
    r = [1]*(i+1)
    for j in range (i+1):
        if j != 0 and j != i:
            r[j] = s[i-1][j-1] + s[i-1][j]
    s.append(r)
for i in s:
    for j in i:
        j = str(j)
        print(j.rjust(6), end='')
    print()