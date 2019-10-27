n = int(input())
s = map(int,input().split())
s = list(s)
ss = []
c = 0
for i in range(n):
    c = c + (max(s)*(i) + 1)
    ss.append(s.index(max(s))+1)
    s[s.index(max(s))] = 0
print(c)
print(' '.join(map(str,ss)))









