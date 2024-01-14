s = 0
for i in range(20):
    if ((i % 2 != 0) and (i != 0) and ((i + 1) % 4 != 0)):
        s = s + 4/i
    elif ((i % 2 != 0) and (i != 0) and ((i + 1) % 4 == 0)):
        s = s - 4/i
    else:
        s = s
print(s)

