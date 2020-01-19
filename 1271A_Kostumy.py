a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if f >= e:
    z = min(b,c,d)
    print(f * z + min((d - z),a) * e )

else:
    y = min(a,d)
    print(e * y + min((d - y),b,c) * f)
