t = int(input())
import math
for i in range(t):
    a,b = map(int,input().split())

    if math.gcd(a,b) != 1:
        print('Infinite')
    else:
        print('Finite')
        

