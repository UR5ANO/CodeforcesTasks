n,v = map(int,input().split())
ba = []
ka = []
for i in range(n):
    t, p = map(int,input().split())
    if t == 1:
        ba.append([i+1,p])
    else:
        ka.append([i+1,p])
 
ba.sort(key=lambda x:x[1], reverse=True)
ka.sort(key=lambda x:x[1], reverse=True)
 
ba_pos = -1
ka_pos = -1
w = 0
while w < v:
    ba_g = -1
    if ba_pos + 1 < len(ba) and w + 1 <= v:
        ba_g = ba[ba_pos + 1][1]
    ka_g = -1
    if ka_pos + 1 < len(ka) and w + 2 <= v:
        ka_g = ka[ka_pos + 1][1]
    if ba_g == -1 and ka_g == -1:
        break
    if ba_g > ka_g / 2:
        ba_pos += 1
        w += 1
    else:
        ka_pos += 1
        w += 2
 
if v - w == 1:
    if ba_pos > -1 and ka_pos + 1 < len(ka):
        if ba[ba_pos][1] < ka[ka_pos + 1][1]:
            ba_pos -= 1
            ka_pos += 1
            w += 1
 
res = ba[:ba_pos + 1] + ka[:ka_pos + 1]
g = sum([r[1] for r in res])
print(g)
print(' '.join([str(r[0]) for r in res]))
