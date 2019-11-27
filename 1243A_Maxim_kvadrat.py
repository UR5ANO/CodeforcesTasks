k = int(input())

for j in range(k):
    n = int(input())
    a = map(int,input().split())
    a = list(a)
    a = sorted(a)
    a.reverse()

    c = 0
    for i in range(len(a)):
        c = c + 1
        if c == a[i]:
            print(c)
            break

        elif c > a[i]:
            print(c - 1)
            break

        else:
            continue
