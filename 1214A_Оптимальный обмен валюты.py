n = int(input())
d = int(input())
e = int(input())*5
 
s = []

if e > n:
    otv = n % d
elif d > n:
    otv = n % e

else:
    for i in range(d+2):
        p = e * i
        if p > n:
            break
        k = (n - p) % d
        s.append(k)
        
    otv = min(s)
print(otv)

