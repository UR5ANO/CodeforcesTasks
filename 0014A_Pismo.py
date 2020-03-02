n,m = map(int,input().split())
s = []
ss = []
for i in range(n):
    c = list(input())
    s.append(c)

a = None
b = None
for i in range(len(s)):
    if '*' in s[i]:
        if a is None:
            a = i
        b = i
s = s[a:b+1]
 
c = None
d = None

for j in range(m):
    
    for i in range(len(s)):
        if s[i][j] == '*':
            
            if c is None:
                c = j
            d = j


for i in range(len(s)):
    print("".join(s[i][c:d+1]))    #"".join(map(str, ss))  можно так



