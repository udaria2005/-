n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
def IsSymmetric(A):
    c = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j and A[i][k] == A[k][j]:
                    c = c+1;
    if c == n**2:
        print('YES')
    else:
        print('NO')
IsSymmetric(a)
