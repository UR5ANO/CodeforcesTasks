T = int(input())
ss = []
for i in range(T):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    s.remove(max(s))
    c = max(s)
    s.remove(max(s))
    
    if len(s) < c:
        ss.append(len(s))
    else:
        ss.append(c-1)

for i in range(len(ss)):
    print(ss[i])
