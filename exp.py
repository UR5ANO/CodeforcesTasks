q = int(input())
for i in range(q):
    n,r = map(int,input().split())
    s = map(int,input().split())
    s = list(s)
    a = set(s)
    s = list(a)
    c = 0
    
    while max(s) > 0:
        for i in range(len(s)):
            s[i] = s[i] - r
        

        s.pop(-1)
        c = c + 1

    print(c)


