s = map(int,input().split())
s = list(s)
x = sum(s)

if x % 2 != 0:
    print('NO')
else:
    a = max(s)
    s.remove(a)
    if a == x / 2:
        print('YES')
    else:
        d = False
        for i in range(3):
            if s[i] + a == x / 2:
                print('YES')
                d = True
                break
            else:
                continue
        if d == False:
            print('NO')

