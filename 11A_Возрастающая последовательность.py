n,d = map(int,input().split())

s = list(map(int,input().split()))
ss = []
for i in range(n-1):
    if s[i] >= s[i+1]:
        k = (s[i] - s[i+1]) // d
        ss.append((k+1)*d)
        s[i+1] = s[i+1]+(k+1)*d
    else:
        continue
        
          
print(int(sum(ss)/d))
