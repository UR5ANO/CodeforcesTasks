y,w = map(int,input().split())

n = 7 - max(y,w)

import math
k = math.gcd(n,6)
x = n//k
y = 6//k

#print(f'{x}/{y}')
print('{}/{}'.format(x,y))





