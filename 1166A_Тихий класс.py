
s = []
for i in range(n):
    ss = list(input())
    s.append(ord(ss[0]))

a = {}
for i in range(len(s)):
    if s[i] in a:
        p = a.get(s[i]) + 1
        a[s[i]] = p
    else:
        a[s[i]] = 1

s = list(a.values())
a = []
b = []

for i in range(len(s)):
    if s[i] <= 1:
        continue
    elif s[i] % 2 == 0:
        l = int(s[i] / 2)
        a.append(l)
        b.append(l)
    else:
        r = int(s[i] // 2)
        rr = int(s[i] % 2)
        a.append(r)
        b.append(r+rr)

def deti(c):
    x = 0
    for i in range(len(c)):
        x = x + (c[i]*(c[i]-1))/2
    return int(x)

deti(a)
deti(b)
print(deti(a)+deti(b))
