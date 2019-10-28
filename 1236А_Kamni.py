t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())

    def kamni(x,y):
        ky = y//2
        kx = x
        q = min(ky,kx)
        p = q * 3
        return p

    kamni(b,c)
    r = kamni(b,c) 
    b = b - (kamni(b,c)/3)
    
    kamni(a,b)
    l = kamni(a,b)
    print(int(l + r))
