T = int(input())
for i in range(T):
    n,d = map(int,input().split())

    res = (n-1)**2 - 4 * (d - n)
    if res < 0:
        print('NO')
    else:
        print('YES')
