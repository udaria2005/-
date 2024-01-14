def ReduceFraction(n,m):
    a = 0
    if n < m:
        a = n
    else:
        a = m
    for i in range(a, 1, -1):
        if n % i == 0 and m % i == 0:
            z = i
            n = n//z
            m = m//z 
    print(n,'',m)
    
p = int(input())
q = int(input())
ReduceFraction(p,q)
                
                