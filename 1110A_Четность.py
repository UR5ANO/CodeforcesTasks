b,k = input().split()
b = int(b)
k = int(k)
a = map(int,input().split(' '))
a = list(a)

n = 0
for i in a:
    n = n * b + i
    n = n % 2
    
if n % 2 == 0:
    print('even')
else:
    print('odd')
