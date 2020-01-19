t = int(input())
for i in range(t):
    p = input()
    p = list(p)
    h = input()
    h = list(h)
    res = False
    for j in range(len(h)-len(p)+1):
        if sorted(h[j:j+len(p)]) == sorted(p):
            print('Yes')
            res = True
            break

    if res == False:
        print('No')
            
    
