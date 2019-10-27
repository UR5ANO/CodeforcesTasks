t = int(input())
u = []
for i in range(t):
    b,p,f = map(int,input().split())
    h,c = map(int,input().split())
    if b % 2 == 0:
        b = b
    else:
        b = b - 1

    if (p * 2) + (f * 2) <= b:
        w = (p * h ) + (f * c)
    else:
        if h <= c:
            if f * 2 <= b:
                q = f * c
                b = b - (f * 2)
                if p * 2 <= b:
                    w = q + (p * h)
                else:
                    w = q + (b/2) * h
            else:
                w = b/2 * c
        else:
            if p * 2 <= b:
                q = p * h
                b = b - (p * 2)
                if f * 2 <= b:
                    w = q + (f * c)
                else:
                    w = q + (b/2) * c
            else:
                w = b/2 * h
    u.append(int(w))

for i in range(len(u)):
    print(u[i])
