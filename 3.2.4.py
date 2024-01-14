n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
      for k in range(n):
          if j == i+k or i == j+k:
              a[i][j] = k
                
for row in a:
    for elem in row:
       print(elem, end=' ')
    print()