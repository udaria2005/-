n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
def SwapCulomns(a,i,j):
    for k in range(n):
        l = int(a[k][i])
        q = int(a[k][j])
        a[k][i] = q
        a[k][j] = l
        
h, b = [int(i) for i in input().split()]
SwapCulomns(a,h,b)
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()