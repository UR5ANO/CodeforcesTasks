n = int(input())
s = map(int,input().split(' '))
s = list(s)

b = []
m = 1
for i in range(n-1):
    
    if s[i] == s[i+1]:
        m = m + 1
                 
    else:
        b.append(m)
        m = 1
        
b.append(m)    
     
c = []
for i in range(len(b)):
    if b[i] <= b[i+1]:
        c.append(2*b[i])
    
    else:
        c.append(2*b[i+1])
    if i == len(b) - 2:
        break
    
print(max(c))
