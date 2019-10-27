a = map(int,input())
a = list(a)

s = 0
for i in range(len(a)):
    s = s + a[i]
    
if s % 4 == 0:
    print(''.join(map(str,a)))
else:
    while s % 4 != 0:
        a = ''.join(map(str,a))
        a = int(a)
        a = a + 1
        a = map(int,str(a))
        a = list(a)
                
        s = 0
        for i in range(len(a)):
            s = s + a[i]
            
    print(''.join(map(str,a)))


