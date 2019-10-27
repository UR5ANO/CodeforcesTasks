l,r = map(int,input().split())
q = False
for i in range(l,r+1):
    if q == True:
        break
    else:
        
        s = map(int,str(i))
        s = list(s)
        c = 0
        for j in range(len(s)):
            if s.count(s[j]) == 1:
                c = c + 1
                if c == len(s):
                    print(''.join(map(str,s)))
                    q = True
                    break
                else:
                    continue
            else:
                break
if q == False:
    print(-1)

