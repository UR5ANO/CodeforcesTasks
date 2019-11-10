n = int(input())
s = map(int,input().split())
s = list(s)
s.sort()
 
import math
minim = 0
for i in range(math.floor(len(s)/2)):
        minim = minim + s[i]
 
s.reverse()
maxim = 0
for i in range(math.ceil(len(s)/2)):
        maxim = maxim + s[i]
 
print(minim**2 + maxim**2)
