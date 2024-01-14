from math import sqrt
s = 0
for i in range(11):
    if (i != 0):
        s = s + 1/(i**2)
    else:
        s = s
p = sqrt(s) * sqrt(6)
print(p)
