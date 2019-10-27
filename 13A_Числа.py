n = int(input())

s = []
z = 0
for i in range(2,n):
    
    l = n%i
    z = n//i
    s.append(l)
    if z < i:
        s.append(z)
        continue
    else:
        while True:
            l = z%i
            z = z//i
            s.append(l)
            
            if z < i:
                s.append(z)
                break
    
x = sum(s)
y = n - 2
import math 
k = math.gcd(x,y)
x = x / k
y = y / k
x = int(x)
y = int(y)
print(f'{x}/{y}')
