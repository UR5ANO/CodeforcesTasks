n,h,m = map(int,input().split())
a = {}

for i in range(n):
    a[i+1] = h
b = {}
for i in range(m):
    l,r,x = map(int,input().split())
    i = l
    
    while i < r + 1:
        b[i] = x
        if b[i] < a[i]:
            a[i] = b[i]
        i = i + 1
        
b = []
for i in a.values():
    b.append(i)

s = 0
for i in range(len(b)):
    s = s + b[i] ** 2

print(s) 


