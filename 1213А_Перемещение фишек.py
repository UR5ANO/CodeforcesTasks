n = int(input())

s = map(int,input().split())
s = list(s)

chet = []
nechet = []
for i in range(n):
    if s[i] % 2 == 0:
        chet.append(s[i])
    else:
        nechet.append(s[i])

if len(chet) <= len(nechet):
    print(len(chet))
else:
    print(len(nechet))





