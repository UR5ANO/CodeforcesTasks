def chisla():
    p = input().split(' ')
    return int(p[0]), int(p[1])

n, t = chisla()
min_t = 1e7
nom = None
for i in range(n):
    s, d = chisla()
    if t < s:
        z = s-t
    else:
        x = (t-s)%d
        if x == 0:
            z = 0
        else:
            z = d - x
    if z < min_t:
        min_t = z
        nom = i + 1

print(nom)
