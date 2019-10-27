#print('"Покупка воды"')
#print('Введите n,a,b')

q=int(input())
i=0
while i<q:
    vvod=input()
    n,a,b=list(map(int,vvod.split()))
    
    k=b/a
    if k>=2:
        print(a*n)
    elif n%2!=0:
        y=int(n//2*b+a)
        print(y)
    else:
        z=int(n/2*b)
        print(z)
    i=i+1
    
