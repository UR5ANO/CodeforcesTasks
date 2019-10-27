n = int(input())
s = map(int,input().split())
s = list(s)

ss = []
a = min(s)
b = max(s)
ss.append(s.index(min(s))+1)
ss.append(s.index(max(s))+1)
c = 0
for i in range(n):
    if s[i] > a and s[i] < b:
        ss.insert(1,s.index(s[i])+1)
        c = c + 1
        break
    else:
        continue

if c == 0:
    print('-1','-1','-1')
else:
    print(ss[0],ss[1],ss[2])
    
