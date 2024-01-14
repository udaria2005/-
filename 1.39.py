u=int(input())
k=2
while k**2<=u and u%k!=0:
    k+=1
if u%k!=0:
    k=u
print(k) 