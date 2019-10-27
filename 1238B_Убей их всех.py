q = int(input())
for i in range(q):
    n,r = map(int,input().split())
    s = map(int,input().split())
    s = list(s)
    s = set(s)
    s = list(s)
    s.sort()
    s.reverse()
    c = 0
    
    for j in s:
        if j - (r * c) <= 0:
            break
        else:
            c = c + 1
            continue
        
    print(c)
