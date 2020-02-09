t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    s = [int(x) for x in s]
    ss = []
    sum = 0
    c =False
    for i in range(len(s)):
        sum += s[i]
        if sum % 2 == 0 and s[i] % 2 != 0:
            ss.append(s[i])
            c = True
            break

        else:
            ss.append(s[i])
            
    if c == True:
        print(''.join(map(str,ss)))

    else:
        print(-1)

        
