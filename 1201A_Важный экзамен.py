n,m = map(int,input().split())
s = []

for i in range(n):
    ss = input()
    ss = list(ss)
    s.append(ss)

sss = map(int,input().split())
sss = list(sss)

d = []
e = []
g = []
for j in range(m):
    for i in range(n):
        d.append(s[i][j])
    e.append(d.count('A'))
    e.append(d.count('B'))
    e.append(d.count('C'))
    e.append(d.count('D'))
    e.append(d.count('E'))
    g.append(max(e))
    e.clear()
    d.clear()

c = 0
for i in range(len(g)):   
    c = c + (g[i] * sss[i])

print(c)
    
    
    
