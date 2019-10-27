n,x,y = map(int,input().split())

s = map(int,input().split())
s = list(s)

for i in range(x,len(s)):
    f = True
    
    for j in range(i-x,i+y+1):
        if s[i] <= s[j]:
            continue
        else:
            f = False
            break
    print(i)    
    if f == True:
        print(i+1)
        break
    else:
        continue
if f == False:
    print(i+1)
#print(s)

