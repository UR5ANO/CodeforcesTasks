t = int(input())

for i in range(t):
    n = int(input())
    p = map(int,input().split())
    p = list(p)
    m = int(input())
    q = map(int,input().split())
    q = list(q)

    p0 = 0
    p1 = 0
    for k in range(len(p)):
        if p[k] %2 == 0:
            p0 = p0 + 1
        else:
            p1 = p1 + 1

    q0 = 0
    q1 = 0
    for j in range(len(q)):
        if q[j] % 2 == 0:
            q0 = q0 + 1
        else:
            q1 = q1 + 1

    print(p0 * q0 + p1 * q1)



