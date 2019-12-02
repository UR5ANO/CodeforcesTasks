n = int(input())
s = map(int,input().split())
s = list(s)

ss = []
ss.append(abs(s[n-1] - s[0]))
for i in range(len(s)-1):
    ss.append(abs(s[i] - s[i+1]))

q = min(ss)

if abs(s[n-1] - s[0]) == q:
    print(n,1)
else:
    for i in range(len(s)-1):
        if abs(s[i] - s[i+1]) == q:
            print(i+1,i+2)
            break
