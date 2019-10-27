n,m,a = map(int,input().split())

if n/a <= 1:
    k = 0
elif n%a == 0:
    k = n/a
else:
    k = n//a + 1

if m/a <= 1:
    p = 0
elif m%a == 0:
    p = m/a
else:
    p = m//a + 1

if k + p == 0:
    print('1')
elif k == 0 or p == 0:
    print(int(k + p))
else:
    print(int(k * p))

    

