n = int(input())
S = []
for i in range(n):
    s = map(int,input().split())
    s = list(s)
    S.extend([s])

SS = []
for i in range(n):
    for j in range(S[i][0]):
        SS.append([i+1,S[i][j+1]])

c = 0
SSS = []
for i in range(len(SS)):
    a = SS[i]
    a = reversed(a)
    a = list(a)
    
    if a in SS:
        continue
    else:
        c = c + 1
        SSS.append(a)

print(c)
for i in range(len(SSS)):
    print(SSS[i][0],SSS[i][1])
