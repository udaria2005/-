s = input()
a = s.find('f')
b = s.find('f',a+1)
s1 = s[:a]+s[b:]