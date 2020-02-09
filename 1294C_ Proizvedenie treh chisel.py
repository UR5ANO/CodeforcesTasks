t = int(input())
import math 
for i in range(t):
    n = int(input())
    res = []
    c = 0
    a = 0
    q = int(math.sqrt(n)) + 2
    
    for j in range(2,q):
        if n % j == 0:
            n = n // j
            res.append(j)
            a = j + 1
            c += 1
            break
    if c == 1:
        q = int(math.sqrt(n)) + 2
        for j in range(a,q):
            if n % j == 0:
                n = n // j
                res.append(j)
                c += 1
                break
        
    if c < 2 or res[0] == n or res[1] == n:
        print('No')
    else:
        print('Yes')
        print(res[0],res[1],n)
            
