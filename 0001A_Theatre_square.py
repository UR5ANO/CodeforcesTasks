import math

n, m, a = map(int, input().split())

k = math.ceil(n / a)
p = math.ceil(m / a)

print(k * p)
