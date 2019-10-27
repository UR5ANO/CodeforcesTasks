n,I = map(int,input().split())

s = map(int,input().split())
s = list(s)

K = max(s) - min(s) + 1

import math
k = math.log2(K)
k = math.ceil(k)
print(k)
if n * k <= I * 8:
    print('0')
else:
    z = n * k - I * 8
    if z % 2 == 0:
        print(int(z/2))
    else:
        print(int(z/2 + 1))


