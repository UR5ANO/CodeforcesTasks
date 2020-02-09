t = int(input())

for i in range(t):
    s = [[0,0]]
    res = []
    n = int(input())
    for j in range(n):
        x,y = map(int,input().split())
        s.append([x,y])

    s = sorted(s)
    c = True
    for j in range(len(s)-1):
        xi = s[j+1][0] - s[j][0]
        yi = s[j+1][1] - s[j][1]
        if xi < 0 or yi < 0:
            print('NO')
            c = False
            break
        else:
            sss = 'R' * xi + 'U' * yi
            res.append(sss)

    if c == True:
        print('YES')
        print(''.join(res))
