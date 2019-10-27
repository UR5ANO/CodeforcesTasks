vvod = input()
x1,x2,x3,x4 = vvod.split()
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
x4 = int(x4)
s = [x1,x2,x3,x4]
z= max(s)
s.remove(max(s))
y = z - s[0]
w = z - s[1]
q = z - s[2]
print(q, w, y)
