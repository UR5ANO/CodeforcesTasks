t = int(input())
for i in range(t):
    a, b, x, r = map(int,input().split())
    a, b = (a, b) if a < b else (b, a)
    c, d = x - r, x + r
    nachalo = c - a
    nachalo = max(0, nachalo)
    nachalo = min(b - a, nachalo)
    konec = b - d
    konec = max(0, konec)
    konec = min(b - a, konec)
    print(nachalo + konec)
