s = input()
t = input()

import math
b = ord(t[0]) - ord(s[0])
b_mod = math.fabs(b)
c = int(t[1]) - int(s[1])
c = int(c)
c_mod = math.fabs(c)
otvet = max(b_mod,c_mod)
print(int(otvet))

while b_mod != c_mod:
    if c_mod < b_mod:
        if b > 0:
            b_mod = b_mod - 1
            print('R')
        else: 
            b_mod = b_mod - 1
            print('L')
        
    else:
        if c > 0:
            c_mod = c_mod - 1
            print('U')
        else:
            c_mod = c_mod - 1
            print('D')

while c_mod > 0 and b_mod > 0:
    if c > 0 and b >0:
        c_mod = c_mod - 1
        b_mod = b_mod - 1
        print('RU')
    elif c > 0 and b < 0:
        c_mod = c_mod - 1
        b_mod = b_mod - 1
        print('LU')
    elif c < 0 and b < 0:
        c_mod = c_mod - 1
        b_mod = b_mod - 1
        print('LD')
    else:
        c_mod = c_mod - 1
        b_mod = b_mod - 1
        print('RD')


