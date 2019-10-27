q = int(input())
ss = []
for i in range(q):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    x = sum(s) / n
    ss.append(x)
import math
for i in range(len(ss)):
    print(math.ceil(ss[i]))
