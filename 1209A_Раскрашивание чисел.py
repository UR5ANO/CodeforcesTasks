n = int(input())
s = map(int,input().split())
s = list(s)
ss = s.copy()
c = 0
while len(s) != 0:
    a = min(s)
    
    for i in range(len(s)):
        if s[i] % a == 0:
            ss.remove(s[i])
        else:
            continue
    s = ss.copy()
    c = c + 1
    
print(c)








