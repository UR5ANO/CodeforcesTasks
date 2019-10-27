n,k = map(int,input().split())
s = []
for i in range(n):
    a = int(input())
    s.append(a)

ss = []
for i in range(1,k+1):
    b = s.count(i)
    ss.append(b)

res = 0
p = 0
for i in range(len(ss)):
    if ss[i] % 2 == 0:
        res = res + ss[i]
    else:
        res = res + ss[i] - 1
        p = p + 1
if p % 2 == 0:
    res = res + p/2
else:
    res = res + p//2 + 1
print(int(res))



