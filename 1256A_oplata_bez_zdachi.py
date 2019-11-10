q = int(input())

for i in range(q):
    a,b,n,S = map(int,input().split())

    if S//n <= a:
        if S%n <= b:
            print('YES')
        else:
            print('NO')
    else:
        if S - a * n <= b:
            print('YES')
        else:
            print('NO')
