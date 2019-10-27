n = int(input())
s = input()
s = list(s)


for i in range(len(s)):
    if s[i] == '+':
        s[i] = 1

    else:
        s[i] = -1

k = 0
for i in range(len(s)):
    k = k + s[i]
    if k < 0:
        k = k + 1
if k > 0:
    print(k)
else:
    print('0')
