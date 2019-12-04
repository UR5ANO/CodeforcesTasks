with open('input.txt','r') as f:
    vvod = f.read()

vvod = vvod.strip().split('\n')
n = int(vvod[0])
s = []

for i in range(n):
    if vvod[1][i] == '1':
        s.append(i)

ss = []
for i in range(len(s)-1):
    ss.append(s[i+1]-s[i])

c = True        
for i in range(len(ss)-1):
    if ss[i] == ss[i+1]:
        continue
    else:
        c = False
        with open('output.txt','w') as f:
            f.write('NO')
            break
if c == True:
    with open('output.txt','w') as f:
        f.write('YES')
