T = int(input())
ss = []
for i in range(T):
    n,s,t = map(int,input().split())
    if s == n and t == n:
        ss.append(1)
    else:
        a = n - s + 1
        b = n - t + 1
        y = max(a,b)
        ss.append(y)

for i in range(T):
    print(ss[i])
