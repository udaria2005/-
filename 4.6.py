s = input()
a = s.find('f')
b = s.find('f',a+1)
if b == -1 and a != -1:
    print(-1)
elif a == -1:
    print(-2)
else:
    print(b)
    