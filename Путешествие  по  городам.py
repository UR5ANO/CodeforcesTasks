#print('введите n v')
vvod=input()
n,v=vvod.split()
n=int(n)
v=int(v)
if v >= n-1:
    s = n-1
    print(s)
else:
    x = n - 1 - v  #нужно литров со 2-го и далее
    i = 1
    s = 0
    while i <= x:
        s = i + 1 + s       
        i = i + 1
    s = v + s
    print(s)
    
     
    

