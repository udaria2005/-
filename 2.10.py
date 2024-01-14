def stepen(a,n):
    c = a**n 
    if c - int(c) != 0:
        print(c)
    else:
        print(int(c))
x = float(input())
y = int(input())
stepen(x,y)