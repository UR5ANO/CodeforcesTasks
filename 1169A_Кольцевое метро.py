n,a,x,b,y = map(int,input().split())

s = []
if a < x:
    for i in range(a,x+1):
        s.append(i)
else:
    for i in range(a,n+1):
        s.append(i)
    for i in range(1,x+1):
        s.append(i)
        
ss = []
if y < b:
    for i in range(y,b+1):
        ss.append(i)
    ss.reverse()
else:
    for i in range(y,n+1):
        ss.append(i)
    for i in range(1,b+1):
        ss.append(i)
    ss.reverse()

k = min(len(s),len(ss))

for i in range(k):
    if ss[i] == s[i]: 
        print('YES')
        break
else:
    print('NO')
