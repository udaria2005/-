s = input()
a = s.find('f')
b = s.rfind('f')
if a == b and a != -1:
    print(a)
elif a != b:
    print(a,b)
else:
    print('')
    