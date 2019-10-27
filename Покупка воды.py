#print('"Покупка воды"')
q=int(input('Сколько строк?', ))
i=0
while i<q:
    n=int(input('Сколько нужно литров?', ))
    a=int(input('Сколько стоит 1л бутылка?', ))
    b=int(input('Сколько стоит 2л бутылка?', ))
    k=b/a
    if k>=2:
        print(a*n)
    elif n%2!=0:
        print(n//2*b+a)
    else:
        print(n/2*b)
    i=i+1

