n = int(input())

if n % 2 == 0:
    print('NO')
elif n == 1:
    print('YES')
    print(1,2)
else:
    sl = []
    sr = []
    s = []
    sl.append(1)
    sl.append(n*2)
    sr.append(2)

    for i in range(n*2-1,2,-1):
        s.append(i)
    c = 0
    for i in range(len(s)):
        if c < 2:
            sr.append(s[i])
            c = c + 1
        elif c == 2:
            sl.append(s[i])
            c = c + 1
        elif c == 3:
            sl.append(s[i])
            c = 0
    
    ss = sl + sr
    print('YES')
    print(" ".join(map(str,ss)))
