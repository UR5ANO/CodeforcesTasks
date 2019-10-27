n,m = map(int,input().split())
s = []
for i in range(n):
    c = list(input())
    s.append(c)
ss = []    
k = 0
for i in range(len(s)):
    p = s[i][0]
    ss.append(p)
    if s[i].count(p) == m:
        k = k + 1
        
        if k == n:
            c = 0
            for i in range(len(ss)-1):
                if ss[i] == ss[i+1]:
                    print('NO')
                    break
                else:
                    c = c + 1
               
        else:
            continue
    else:
        print('NO')
        break
        
if c == len(ss)-1:
    print('YES')

    

