n = 8
s = []
for i in range(n):
    c = list(input())
    s.append(c)

answer = 0    
for i in range(8):
    count = 0
    for j in range(8):
        if s[i][j] == 'B':
            count = count + 1
    if count == 8:
        answer = answer + 1

if answer == 8:
    print(answer)
        
else:
    for i in range(8):
        count = 0
        for j in range(8):
            if s[j][i] == 'B':
                count = count + 1
     
        if count == 8:
            answer = answer +1
    print(answer)


