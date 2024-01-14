n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
k = int(a[0][0])
i1 = 0
j1 = 0
for i in range (n):
    for j in range (m):
        if int(a[i][j]) > k:
            k = a[i][j]
            i1 = i
            j1 = j
print(i1,j1)