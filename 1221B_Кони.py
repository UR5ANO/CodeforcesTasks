n = int(input())
s = []
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            s.append('W')
        else:
            s.append('B')
    print(''.join(s))
    s.clear()

    
