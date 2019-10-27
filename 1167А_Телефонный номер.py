t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input())
    s = list(s)
    o = 8 in s
    
    if o == False or n - s.index(8) < 11:
        print('NO')
    else:
        print('YES')
