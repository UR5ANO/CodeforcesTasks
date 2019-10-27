t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    p = 0
    if b == 0 or c < 2:
        p = p + 0
        if a < 1 or b < 2:
            p = p + 0
        else:
            p = p + b//2 + 2*(b//2)
    else:
        if c%2 == 0:
            c = c
        else:
            c = c - 1

        if c/2 == b:
            p = b + c

        elif c/2 < b:
            p = c/2 + c
            b = b - c/2
            if b < 2 or a < 1:
                p = p
            else:
                p = p + b//2 + 2*(b//2)

        elif c/2 > b:
            p = b + (b * 2)
        
    print(int(p))
