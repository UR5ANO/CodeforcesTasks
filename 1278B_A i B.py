t = int(input())
import math
for i in range(t):
    a,b = map(int,input().split())
    w = int(math.fabs(a-b))

    if a == b:
        print(0)
        
    elif w % 2 == 0:
        c = 0
        for j in range(1,1000000):
            if c >= w and c % 2 == 0:
                break
            else:
                c += j
        print(j-1)

    elif w % 2 != 0:
        c = 0
        for j in range(1,1000000):
            if c >= w and c % 2 != 0:
                break
            else:
                c += j
        print(j-1)
