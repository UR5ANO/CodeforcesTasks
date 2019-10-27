n = int(input())
s = []
bal = dict()
g_zab = dict()
g_pr = dict()
k = 0
for i in range(1,n):
    k = k + i

for i in range(n):
    c = input()
    s.append(c)

for i in range(k):
    a1,b1 = input().split()
    k1,k2 = a1.split('-')
    c1,c2 = b1.split(':')
    c1 = int(c1)
    c2 = int(c2)
    if k1 in g_zab:
        g_zab[k1] = g_zab.get(k1) + c1
    else:
        g_zab[k1] = c1
    if k2 in g_zab:
        g_zab[k2] = g_zab.get(k2) + c2
    else:
        g_zab[k2] = c2    


    if k1 in g_pr:
        g_pr[k1] = g_pr.get(k1) + c2
    else:
        g_pr[k1] = c2
    if k2 in g_pr:
        g_pr[k2] = g_pr.get(k2) + c1
    else:
        g_pr[k2] = c1    

     
    if c1 == c2:
        if k1 in bal:
            bal[k1] = bal.get(k1) + 1
        else:
            bal[k1] = 1
        if k2 in bal:
            bal[k2] = bal.get(k2) + 1
        else:
            bal[k2] = 1   
    elif c1 > c2:
        if k1 in bal:
            bal[k1] = bal.get(k1) + 3
        else:
            bal[k1] = 3
        if k2 in bal:
            bal[k2] = bal.get(k2) + 0
        else:
            bal[k2] = 0  
    else:
        if k2 in bal:
            bal[k2] = bal.get(k2) + 3
        else:
            bal[k2] = 3
        if k1 in bal:
            bal[k1] = bal.get(k1) + 0
        else:
            bal[k1] = 0    

spisok = []
for name in s:
    ch = bal[name]
    razn = g_zab[name] - g_pr[name]
    zab = g_zab[name]
    ss = [ch,razn,zab,name]
    spisok.append(ss)
    
spisok = sorted(spisok)

spisok = spisok[int(n/2):]
com = [e[3] for e in spisok]
com = sorted(com)


for e in com:
    print(e)

