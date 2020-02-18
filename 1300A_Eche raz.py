t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)

    res = s.count(0) + sum(s)
    if res == 0:
        print(s.count(0) + 1)
    else:
        print(s.count(0))
