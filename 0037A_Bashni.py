N = int(input())
s = map(int,input().split())
s = list(s)
a = set(s)

ss =[]
for i in a:
    ss.append(s.count(i))

print(max(ss),len(a))


