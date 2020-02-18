T = int(input())
import math
for i in range(T):
    n,g,b = map(int,input().split())

    gx = math.ceil(n/2)
    bx = n // 2
    C = math.ceil(gx / g)
    if (C - 1) * b >= bx:
        print((C - 1) * b + gx)

    else:
        print((C - 1) * b + gx + (bx - (C - 1) * b))
