n,k = map(int,input().split())
s = input()
s = list(s)
if n == 1 and k > 0:
    print(int(0))

elif k == 0:
    print(''.join(map(str,s)))
    
else:
    c = 0
    if s[0] > '1':
        s[0] = 1
        c = c + 1
    
    for i in range(1,len(s)):
        if c == k:
            break
        if s[i] == '0':
            continue
        else:
            s[i] = 0
            c = c + 1

    print(''.join(map(str,s)))
