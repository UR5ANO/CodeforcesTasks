first_line=input()
x,y,z=first_line.split()
x=int(x)
y=int(y)
z=int(z)
second_line=input()
a,b,c=second_line.split()
a=int(a)
b=int(b)
c=int(c)
P=a-x
if P>=0:
    K=P+b-y
    if K>=0:
        M=K+c-z
        if M>=0: 
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')   
