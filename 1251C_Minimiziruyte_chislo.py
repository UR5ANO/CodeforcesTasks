t = int(input())

for i in range(t):
    chet = []
    nechet = []
    res = []
    a = input()
    a = list(a)
    for j in a:
        j = int(j)
        if j % 2 == 0:
            chet.append(j)
        else:
            nechet.append(j)

    chet_pos = 0
    nechet_pos = 0

    while chet_pos < len(chet) and nechet_pos < len(nechet):
        if chet[chet_pos] < nechet[nechet_pos]:
            res.append(str(chet[chet_pos]))
            chet_pos += 1
        else:
            res.append(str(nechet[nechet_pos]))
            nechet_pos += 1
    for j in range(chet_pos,len(chet)):
        res.append(str(chet[j]))
    for j in range(nechet_pos,len(nechet)):
        res.append(str(nechet[j]))

    print("".join(res))


