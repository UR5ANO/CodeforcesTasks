
n=100
D=set()
for s in range(1,n+1):
    if s%5==2 or s%5==4:
        if s%7==3:
            if s%3!=1:
                D.add(s)

print(D)

print('good luck!')
