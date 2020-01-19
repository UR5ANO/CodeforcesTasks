n,m = map(int,input().split())
s = input()
s = s.split()
t = input()
t = t.split()
q = int(input())

for i in range(q):
    y = int(input())
    res_s = y % len(s)
    res_t = y % len(t)
    print(s[res_s-1] + t[res_t-1])
