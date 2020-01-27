t = int(input())
for i in range(t):
    n,s,k = map(int,input().split())
    ss = map(int,input().split())
    ss = list(ss)
    
    R = s
    while R < n + 1:
        if R in ss:
            R = R + 1
        else:
            break
    
    L = s
    while L > 0:
        if L in ss:
            L = L - 1
        else:
            break

    if L < 1 and R > n:
        print(0)
    elif L < 1:
        print(R - s)
    elif R > n:
        print(s - L)
    else:
        print(min(s - L,R - s))
