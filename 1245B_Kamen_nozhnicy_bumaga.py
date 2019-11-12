t = int(input())
import math
for i in range(t):
    res = 0
    n = int(input())
    a,b,c = map(int,input().split())
    s = input()
    ss = []
    for j in s:
        if j == 'R':
            if b > 0:
                b = b - 1
                ss.append('P')
                res = res + 1
            else:
                ss.append('0')

        elif j == 'P':
            if c > 0:
                c = c - 1
                ss.append('S')
                res = res + 1
            else:
                ss.append('0')

        elif j == 'S':
            if a > 0:
                a = a - 1
                ss.append('R')
                res = res + 1
            else:
                ss.append('0')
    
    if res >= math.ceil(n/2):
        for k in range(len(ss)):
            if ss[k] == '0':
                if a > 0:
                    ss[k] = 'R'
                    a = a - 1
                elif b > 0:
                    ss[k] = 'P'
                    b = b - 1
                elif c > 0:
                    ss[k] = 'S'
                    c = c - 1
        print('YES')
        print("".join(ss))
    else:
        print('NO')
