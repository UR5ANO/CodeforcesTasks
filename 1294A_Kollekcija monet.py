t = int(input())
for i in range(t):
    a,b,c,n = map(int,input().split())
    s = []
    s.extend([a,b,c])
    s.sort()
    q = (s[-1] - s[-2]) + (s[-1] - s[-3])
    if q > n:
        print('No')
    else:
        if (n - q) % 3 == 0:
            print('Yes')
        else:
            print('No')
