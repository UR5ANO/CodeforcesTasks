T = int(input())
ss = []
for i in range(T):
    s,i,e = map(int,input().split())
    if s - i > e:
        otv = e + 1
        ss.append(otv)
    if s - i == e:
        otv = e
        ss.append(otv)
    if s - i < e:
        import math
        otv = math.ceil((e + (s - i))/2)
        if otv <= 0:
            ss.append(0)
        else:
            ss.append(otv)

for i in range(len(ss)):
    print(int(ss[i]))






