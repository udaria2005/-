s = input()
a = s.find('h')
b = s.rfind('h')
s1 = s[:a]+s[b:a:-1]+s[b:]
print(s1)
