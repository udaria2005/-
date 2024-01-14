n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
def IsSymmetric(A):
    s = ''
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j and A[i][k] != A[k][j]:
                    s = 'NO'
                    break;
                elif i == j and A[i][k] == A[k][j]:
                    s = 'YES'
    print(s)
IsSymmetric(a)
if n == 0:
    print('YES')
                    