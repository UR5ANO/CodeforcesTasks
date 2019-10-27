t = int(input())

for i in range(t):
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    c = 0
    p = s[-1]
    for a in s[:-1][::-1]:
        if p < a:
            c = c + 1
        else:
            p = a
    
    print(c)
