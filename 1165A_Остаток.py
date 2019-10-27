n,x,y = map(int,input().split())
s = list(map(int,input()))
s = s[len(s) - x:]
ss = [1]

c = 0
while c < y:
    ss.append(0)
    c = c + 1

k = len(s) - len(ss)
d = 0
while d < k:
    ss[0:0] = [0]
    d = d + 1

m = 0
for i,j in zip(s,ss):
    if i != j:
        m = m + 1
print(m)


