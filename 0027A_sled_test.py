n = int(input())
s = map(int,input().split())
s = list(s)
s.sort()

for i in range(1,3002):
    if i in s:
        continue
    else:
        print(i)
        break

