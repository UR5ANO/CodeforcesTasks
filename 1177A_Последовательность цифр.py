k = int(input())
c = 0
for i in range(1,10000):
    s = str(i)
    c = c + len(s)
    if c >= k:
        break
    else:
        continue

b = str(i)
if c == k:
    print(b[len(b)-1])
else:
    print(b[len(b)-(c-k)-1])

