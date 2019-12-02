n = int(input())
s = map(int,input().split())
s = list(s)
chet = []
nechet = []

for i in s:
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)

if len(chet) > len(nechet):
    print(s.index(nechet[0])+1)
else:
    print(s.index(chet[0])+1)
