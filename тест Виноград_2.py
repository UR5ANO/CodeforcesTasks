print('Тест "Виноград" ')
def yes():
    print('YES')

def no():
    print('NO')
    
print('Введите x y z', )
x=int(input())  
y=int(input())
z=int(input())

a=3
b=3
c=3
p=a-x
if p>=0:
    k=p+b-y
    if k>=0:
        m=k+c-z
        if m>=0: 
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')   
