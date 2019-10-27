n = int(input())
s = input()

ss = []
a = s.count('n')
for i in range(a):
    ss.append(1)


b = s.count('z')
for i in range(b):
    ss.append(0)

print(' '.join(map(str,ss)))
