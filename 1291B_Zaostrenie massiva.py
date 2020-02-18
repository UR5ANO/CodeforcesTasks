t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)

    lev = 0
    for j in range(len(s)):
        if s[j] >= j:
            lev += 1
        else:
           break

    prav = 0
    s = reversed(s)
    s = list(s)
    for j in range(len(s)):
        if s[j] >= j:
            prav += 1
        else:
            break           

    if lev + prav > len(s):
        print('Yes')
    else:
        print('No')
    
