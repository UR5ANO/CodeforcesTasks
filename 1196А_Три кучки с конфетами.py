q = int(input())
s = []
for i in range(q):
    a,b,c = map(int,input().split())
    k = (a+b+c)//2
    s.append(k)

for i in range(q):
    print(s[i])




