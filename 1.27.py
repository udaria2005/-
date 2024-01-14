a = int(input())
b = int(input())
if a < b:
    i = a
    print(i)
    for i in range (a, b):
        i += 1
        print(i)
else:
    i = a
    print(i)
    for i in range (a, b, -1):
        i -= 1
        print(i)