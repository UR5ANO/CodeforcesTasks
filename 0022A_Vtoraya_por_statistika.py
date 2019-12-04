n = int(input())
s = map(int,input().split())
s = list(s)
s = sorted(s)
   
c = True
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        print(s[i+1])
        c = False
        break
    
if c == True or len(s) < 2:
    print('NO')

    
