q = int(input())

for i in range(q):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    s.sort()
    f = True    
    for j in range(len(s)-1):
        if s[j+1]-s[j] > 1:
            continue
        else:
            f = False
            break
    if f == True:
        print(1)
    else:
        print(2)
        
