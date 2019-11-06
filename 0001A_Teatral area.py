def sravnen(x,y):
    if x/y <= 1:
        res = 0
    elif x%y == 0:
        res = x/y
    else:
        res = x//y + 1
    return res 

n,m,a = map(int,input().split())

k = sravnen(n,a)
p = sravnen(m,a)

if k + p == 0:
    print('1')
elif k == 0 or p == 0:
    print(int(k + p))
else:
    print(int(k * p))

    

