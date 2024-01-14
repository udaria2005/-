a = int(input())
b = int(input())
c = int(input())

a1 = 0
if a % 2 == 0:
    a1 = a/2
else:
    a1 = a//2 + 1
    
b1 = 0
if b % 2 == 0:
    b1 = b/2
else:
    b1 = b//2 + 1
    
c1 = 0
if c % 2 == 0:
    c1 = c/2
else:
    c1 = c//2 + 1
    
fin = a1 + b1 + c1
f = int(fin)
print(f)