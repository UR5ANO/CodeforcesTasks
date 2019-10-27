vvod=input()
n,m=vvod.split()
n=int(n)
m=int(m)
k=m/n
if k>1 and k%2!=0 and k%3!=0:
    print('-1')
else:
          
    
    c=0
    while k>1:
    
        if k%3==0:
            k=k/3
            c=c+1
            continue
        if k%2==0:
            k=k/2
            c=c+1
            continue
        
        print('-1')
        break
        
    if k==1:
        print(c)
