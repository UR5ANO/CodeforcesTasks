with open('input.txt','r') as f:
    vvod = f.read()

vvod = vvod.strip().split('\n')

txt = int(vvod[0])
s = []
s1 = map(int,vvod[1].split())
s1 = list(s1)
s.append(s1)
s2 = map(int,vvod[2].split())
s2 = list(s2)
s.append(s2)
s3 = map(int,vvod[3].split())
s3 = list(s3)
s.append(s3)

for i in range(3):
    if txt == s[i][0]:
        txt = s[i][1]
    elif txt == s[i][1]:
        txt = s[i][0]

with open('output.txt','w') as f:
    f.write(str(txt))
