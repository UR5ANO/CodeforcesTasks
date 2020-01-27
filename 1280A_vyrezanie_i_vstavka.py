q = int(1e9 + 7)
t = int(input())

for i in range(t):
    x = int(input())
    s = input()
    
    s = [int(p) for p in s]
    c = len(s)
    nul = len(s)
    if x > c:
        s = s + [0] * (x - c) 

    for j,sj in enumerate(s):
        if j == x:
            break
        if sj > 1:
            c = (j + 1 + (c - (j + 1)) * sj) % q 
            if nul < x:
                nul0 = nul       
                for k in range(sj - 1):
                    for l in range(j+1,nul0):
                        if nul == x:
                            break
                        s[nul] = s[l]
                        nul = nul + 1

        
    print(c)
    
    
    
