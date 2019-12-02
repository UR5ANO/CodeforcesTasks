n,d = map(int,input().split())
s = map(int,input().split())
s = list(s)
s.sort()
res = 0
for i in range(len(s)-1):
    q = s[i] + d
    c = 0
    
    for j in range(i+1,len(s)):
        if s[j] <= q:
            c = c + 1
        else:
            break
        
    res = res + c
    
print(2 * res)




    
    
