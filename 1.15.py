n = int(input())
h = n//3600
m = n//60
s = n%60
while (h >= 24):
    h = h - 24
while (m >= 60):
    m = m - 60
h1 = str(h)
m1 = str(m)
s1 = str(s)
if m >= 10 and s >= 10:
    print(h1+':'+m1+':'+s1)
elif m >= 10 and s < 10:
    print(h1+':'+m1+':0'+s1)
elif m < 10 and s < 10:
    print(h1+':0'+m1+':0'+s1)
else:
    print(h1+':0'+m1+':'+s1)