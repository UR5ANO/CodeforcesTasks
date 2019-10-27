x1,y1,x2,y2,x3,y3 = map(int,input().split())
s = []
ss = [[x1-1,y1,x2,y2,x3,y3],[x1+1,y1,x2,y2,x3,y3],[x1,y1-1,x2,y2,x3,y3],[x1,y1+1,x2,y2,x3,y3],[x1,y1,x2-1,y2,x3,y3],[x1,y1,x2+1,y2,x3,y3],[x1,y1,x2,y2-1,x3,y3],[x1,y1,x2,y2+1,x3,y3],[x1,y1,x2,y2,x3-1,y3],[x1,y1,x2,y2,x3+1,y3],[x1,y1,x2,y2,x3,y3-1],[x1,y1,x2,y2,x3,y3+1]]
import math
a1 = x2 - x1
b1 = y2 - y1
a2 = x3 - x2
b2 = y3 - y2
a3 = x3 - x1
b3 = y3 - y1

c1 = math.sqrt(a1*a1+b1*b1)
s.append(c1)
c2 = math.sqrt(a2*a2+b2*b2)
s.append(c2)
c3 = math.sqrt(a3*a3+b3*b3)
s.append(c3)
k = max(s)
s.remove(max(s))

gip = round(k*k,1)
kat = round(s[0]*s[0] + s[1]*s[1],1)
s.clear()
if gip != kat:
    c = 0
    for i in range(12):
        a1 = ss[i][2] - ss[i][0]
        b1 = ss[i][3] - ss[i][1]
        a2 = ss[i][4] - ss[i][2]
        b2 = ss[i][5] - ss[i][3]
        a3 = ss[i][4] - ss[i][0]
        b3 = ss[i][5] - ss[i][1]

        c1 = math.sqrt(a1*a1+b1*b1)
        s.append(c1)
        c2 = math.sqrt(a2*a2+b2*b2)
        s.append(c2)
        c3 = math.sqrt(a3*a3+b3*b3)
        s.append(c3)
        
        if c1 == 0 or c2 == 0 or c3 == 0:
            s.clear()
            c = c + 1
            continue   
        else:
            k = max(s)
            s.remove(max(s))

            gip = round(k*k,1)
            kat = round(s[0]*s[0] + s[1]*s[1],1)
            s.clear()
            c = c + 1
            if gip == kat:
                print('ALMOST')
                break
            if c == 12:
                print('NEITHER')
        
            else:
                continue
        
else:
    print('RIGHT')
