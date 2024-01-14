n = int(input())
a = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == n//2:
            a[i][j] = '*'
        if i == n//2:
            a[i][j] = '*'
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = '*'
for i in range(n):
    for j in range(n):
        if i == n-j-1 or j == n-i-1:
            a[i][j] = '*'
            
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()