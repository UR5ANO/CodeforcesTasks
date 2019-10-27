n = int(input())
s = map(int,input().split())
s = list(s)

ss = [s]


while len(ss) > 0:
    
    a = ss.pop(0)
    flag = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
           k = len(a) // 2
           l = a[0:k]
           r = a[k:len(a)]
           ss.append(l)
           ss.append(r)
           flag = False 
           break 
    if flag:
        print(len(a))
        break
       
    


        



