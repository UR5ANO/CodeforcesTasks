t = int(input())
s = []
ss = []
sss = []
fin = []
import math
for i in range(t):
    n,x = map(int,input().split())
    
    for i in range(n):
        d,h = map(int,input().split())
        s.append(d)
        ss.append(h)
    a = x - max(s)
    for i in range(len(s)):
        b = s[i] - ss[i]
        sss.append(b)

    if a > 0 and max(sss) <= 0:
        print(-1)
    elif a <= 0:
        print(1)
    else:
        otv = math.ceil(a / max(sss)) + 1
        print(otv)
    s.clear()
    ss.clear()
    sss.clear()
    
#for i in range(len(fin)):
#    print(fin[i])

