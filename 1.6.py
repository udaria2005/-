v=int(input())
t=int(input())
a=v*t
if a>0 :
    while a>109:
        a -= 109
    print(a)
else:
    while a<0:
        a += 109
    print(a)
