n = int(input())
si = []
sh = []
res = []
for j in range(n):
    i,h = map(str,input().split())
    si.append(i)
    sh.append(h)

for j in range(len(si)-1):
    if si[j] == si[j+1]:
        res.append(sh[j])

res.append(sh[-1])    
for j in res:
    print(j)
