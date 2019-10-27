c = 0
otvet = 0

import sys
l = list(map(lambda x: x.strip(), sys.stdin.readlines()))

for s in l:
    if s[0] == '+':
        c = c + 1
    elif s[0] == '-':
        c = c - 1
    else:
        p = (len(s) - s.index(':')-1) * c
        otvet = otvet + p
 
print(otvet)
