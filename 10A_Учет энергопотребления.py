n,p1,p2,p3,t1,t2 = map(int,input().split())
ll = []
rr = []
for i in range(n):
    l,r = map(int,input().split())
    ll.append(l)
    rr.append(r)

s = []
for i in range(n):
    if i+1 < n:
        if rr[i] + t1 < ll[i+1]:
            u = (rr[i] - ll[i])*p1 + t1*p1
            s.append(u)
            if rr[i] + t1 + t2 < ll[i+1]:
                p = t2 * p2 + (ll[i+1] - (rr[i]+t1+t2)) * p3
                s.append(p)
            else:
                p = (ll[i+1] - (rr[i] + t1)) * p2
                s.append(p)

        else:
            w = (ll[i+1] - ll[i])*p1
            s.append(w)


    else:
        v = (rr[i] - ll[i]) * p1
        s.append(v)

print(sum(s))        
