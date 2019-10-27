T = int(input())
s = []
for i in range(T):
    n,x = map(int,input().split())
    s.append(2 * x)

for i in range(len(s)):
    print(s[i])
