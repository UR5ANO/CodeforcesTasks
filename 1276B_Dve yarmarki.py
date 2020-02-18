t = int(input())

for _ in range(t):
    n,m,a,b = map(int,input().split())
    e = {}
    for _ in range(m):
        u,v = map(int,input().split())

        if u not in e:
            e[u] = set()
        e[u].add(v)
        
        if v not in e:
            e[v] = set()
        e[v].add(u)

    used = [False] * (n + 1)
    s = [-1] * n
    sl = 0
    sr = 0
    c1,c2 = 0,0
    used[a] = True
    used[b] = True
    start = 1
    while start <= n and used[start]:
        start += 1
           
    while start <= n:
        s[sr] = start
        sr += 1 
        used[start] = True
        c = 0
        da = False
        db = False
        while sl < sr:
            u = s[sl]
            sl += 1
            c += 1
                        
            for v in e[u]:
                if v == a:
                    da = True
                if v == b:
                    db = True
                if not used[v]:
                    s[sr] = v
                    sr += 1
                    used[v] = True

        while start <= n and used[start]:
            start += 1

        if da and not db:
            c1 += c

        if not da and db:
            c2 += c
        
    print(c1 * c2)
