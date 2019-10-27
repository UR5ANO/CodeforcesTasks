s = input()
s = list(s)
x = s.count('1')
import math

if x == 1:
    a = (len(s) - 1)/2
    print(int(math.ceil(a)))
elif x == 0:
    print('0')
else:
    print(int(math.ceil(len(s)/2)))



