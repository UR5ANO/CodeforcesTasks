n = int(input())
s = map(int,input().split())
s = list(s)
c = True
for i in range(len(s)-1):
    if c == False:
        break
    else:
        for j in range(i+1,len(s)):
            q = (s[i] + s[j])
            if q in s:
                print(s.index(q)+1,i+1,j+1)
                c = False
                break
            
if c == True:
    print(-1)
