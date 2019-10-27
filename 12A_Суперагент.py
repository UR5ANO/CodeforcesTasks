s = []
for i in range(3):
    ss = input()
    ss = list(ss)
    s.append(ss)

if s[0][0] == s[2][2] and s[0][1] == s[2][1]\
   and s[0][2] == s[2][0] and s[1][0] == s[1][2]:
    print('YES')
else:
    print('NO')






