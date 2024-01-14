n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
def SwapDiagonals(A):
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j], A[n-j-1][j] = A[n-j-1][j], A[i][j]
            
SwapDiagonals(a)
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()