n, m = [int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]
l = max(n,m)
for i in range(n):
    for j in range(m):
        for k in range(1, l, 2):
            if j == i + k or i == j + k:
                a[i][j] = '*'
                
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()