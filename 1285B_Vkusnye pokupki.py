t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    q = sum(s)
    c = True
    res = 0
    for j in range(n -1):
        res += s[j]
        if res >= q:
            c = False
            break
    
    if c == False:
        print('NO')
    else:
        s = reversed(s)
        s = list(s)
        res = 0
        for j in range(n - 1):
            res += s[j]
            if res >= q:
                c = False
                break
        
        if c == False:
            print('NO')
        else:
            print('YES')
