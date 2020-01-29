t = int(input())
for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    sss = {}
    for i in range(len(s)):
        if s[i] % 2 != 0:
            continue
        else:
            q = s[i]
            c = 0
            while True:
                if q % 2 != 0:
                    if q in sss:
                        if sss[q] < c:
                            sss[q] = c
                        break
                    else:
                        sss[q] = c
                        break
            
                else:
                    q = q // 2
                    c = c + 1
                
  
    print(sum(sss.values()))  
    

    
    
