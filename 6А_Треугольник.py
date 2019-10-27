s = map(int,input().split())
s = list(s)
ss = s.copy()
p = max(s)
s.remove(p)

if p<s[0]+s[1] or p<s[0]+s[2] or p<s[1]+s[2]:
    print('TRIANGLE')
else:        
    o = max(s)  
    s.remove(o)
    if o<s[0]+s[1]:
        print('TRIANGLE')
    elif ss[0]==ss[1]+ss[2] or ss[0]==ss[1]+ss[3] or ss[0]==ss[2]+ss[3] or ss[1]==ss[0]+ss[2] or ss[1]==ss[0]+ss[3] or ss[1]==ss[2]+ss[3] or ss[2]==ss[0]+ss[1] or ss[2]==ss[0]+ss[3] or ss[2]==ss[1]+ss[3] or ss[3]==ss[0]+ss[1] or ss[3]==ss[0]+ss[2] or ss[3]==ss[1]+ss[2]:
        print('SEGMENT')
    else:
        print('IMPOSSIBLE')



