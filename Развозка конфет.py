print('РАЗВОЗКА КОНФЕТ ПО ГОРОДАМ')
print('Введите количество городов и конфет через пробел')
first_line=input()
n,m=first_line.split()
n=int(n)
m=int(m)
#print(n,m)

a=[1,1,2,3]
b=[2,3,3,2]
poezd=[]
#konf=[]
c=0
p=0
while p==n:
    konf=[]
    for i in range(m):
        if a[i]==1:
            konf.append([i,b[i]])
            print(konf)
            k[i],k=max(konf)
            poezd.append(k)
            del a[ki]
            del b[ki]
            print(konf)

            c=c+1
            p=p+1
            if len(a)+len(poezd)==0:
                break
print(poezd)
print(c)
