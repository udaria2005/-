s = input()
while len(s)//2 != 0:
    print(s[(len(s)+1)//2:]+s[:(len(s)+1)//2])
    break;
while len(s)//2 == 0:
    print(s[(len(s))//2:]+s[:(len(s))//2])
    break;