def prostoe(q):
   d = 2
   while q % d != 0:
       d += 1
   return d == q

n = int(input())
s = []

for i in range(2,n):
    if prostoe(i) == True:
        s.append(i)

ss = []
for j in range(2,n+1):
    c = 0
    for i in s:
        if j % i == 0:
            c = c + 1
    if c == 2:
        ss.append(1)
        
print(len(ss))
