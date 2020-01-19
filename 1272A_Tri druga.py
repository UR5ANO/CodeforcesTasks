q = int(input())
for i in range(q):
    a,b,c = map(int,input().split())
    s = []
    s.extend([a,b,c])
    s.sort()
    
    if s[0] == s[1] and s[0] == s[2]:
        print(0)

    elif s[0] == s[1] and s[1] != s[2]:
        if (s[2] - s[1]) > 1:
            s[2] = s[2] - 1
            s[0] = s[0] + 1
            print(2 * (s[2] - s[0]))
        else:
            print(0)

    elif s[0] != s[1] and s[1] == s[2]:
        if (s[1] - s[0]) > 1:
            s[1] = s[1] - 1
            s[0] = s[0] + 1
            print(2 * (s[1] - s[0]))
        else:
            print(0)

    else:
        s[0] = s[0] + 1
        s[2] = s[2] - 1
        print((s[1] - s[0]) + (s[2] - s[0]) + (s[2] - s[1]))
