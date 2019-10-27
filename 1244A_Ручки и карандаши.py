t = int(input())
import math
for i in range(t):
    a,b,c,d,k = map(int,input().split())
    p = math.ceil(a/c)
    q = math.ceil(b/d)
    if p + q <= k:
        print(p,q)
    else:
        print(-1)
