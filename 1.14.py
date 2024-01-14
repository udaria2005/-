n = int(input())

z = n//60
m = n%60
while (z >= 24):
    z = z - 24
print (z,'',m)
