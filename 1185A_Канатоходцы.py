a,b,c,d = map(int,input().split())
s = []
s.append(a)
s.append(b)
s.append(c)
s = sorted(s)

import math
x = 0
y = 0

if math.fabs(s[0] - s[1]) < d:
    x = d - math.fabs(s[0] - s[1])

if math.fabs(s[1] - s[2]) < d:
    y = d - math.fabs(s[1] - s[2])

print(int(x + y))


