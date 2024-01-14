x = int(input())
p = int(input())
y = int(input())
k = 0
while x < y:
    k = k+1
    x = x + (x*0.01*p)
    x = int(x*100)*0.01
print(k)