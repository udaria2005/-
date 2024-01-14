n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
def Transpore(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
            
Transpore(a)
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()