n,t = map(int,input().split())
s = []
for i in range(n):
    x,a = map(int,input().split())
    x1 = x - a/2
    x2 = x + a/2
    s.append([x1,x2])
s.sort()

c = 0
for i in range(n-1):
    if t < s[i+1][0] - s[i][1]:
        c = c + 2
    if t == s[i+1][0] - s[i][1]:
        c = c + 1
c = c + 2    
print(c)
