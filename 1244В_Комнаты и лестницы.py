t = int(input())
ss = []
for i in range(t):
    n = int(input())
    s = input()
    s = list(s)
    
    if s.count('0') == n:
        ss.append(n)
    elif s.count('1') == n:
        ss.append(n*2)
    else:
        a = s.index('1')
        s.reverse()
        b = s.index('1')
        p = min(a,b)
        ss.append((n*2) - (p*2))

for i in ss:
    print(i)









