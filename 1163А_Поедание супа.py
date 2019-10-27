n,m = input().split()
n = int(n)
m = int(m)

if m == 0:
    print('1')
elif n / m >= 2:
    print(m)
else:
    print(n - m)
