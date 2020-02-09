t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    sum = 0
    chet = 0
    nechet = 0
    for i in range(len(s)):
        sum += s[i]
        if s[i] % 2 == 0:
            chet += 1

        else:
            nechet += 1
            
    if sum % 2 != 0:
        print('YES')

    else:
        if chet != 0 and nechet != 0:
            print('YES')

        else:
            print('NO')

        
