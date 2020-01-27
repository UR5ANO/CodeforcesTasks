t = int(input())
for i in range(t):
    s = input()
    ss = []
    c = 0
    j = 0
    while j < len(s)-2:
        if s[j:j+5] == 'twone':
            ss.append(j+3)
            c = c + 1
            j = j + 5

        elif s[j:j+3] == 'two':
            ss.append(j+2)
            c = c + 1
            j = j + 3

        elif s[j:j+3] == 'one':
            ss.append(j+2)
            c = c + 1
            j = j + 3    

        else:
            j = j + 1
    
    print(c)
    print(' '.join(map(str,ss)))
        
