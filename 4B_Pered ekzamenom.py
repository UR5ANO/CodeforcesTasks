d,sum_time = map(int,input().split())
s = []
t_max = 0
t_min = 0
for i in range(d):
    min_time,max_time = map(int,input().split())
    s.append([min_time,max_time])
    t_max = t_max + max_time
    t_min = t_min + min_time

if t_max < sum_time or sum_time < t_min:
    print('NO')
else:
    ss = []
    for i in range(len(s)):
        middle_time = (s[i][0] + s[i][1]) // 2
        ss.append(middle_time)

    import math
    razn = math.fabs(sum(ss) - sum_time)
    razn = int(razn)
    
    if sum(ss) == sum_time:
        print('YES')
        print(' '.join(map(str,ss))) 

    elif sum(ss) < sum_time:
        c = 0
        for i in range(d):
            if c == razn:
                break
            else:
                while ss[i] < s[i][1]:
                    ss[i] = ss[i] + 1
                    c = c + 1
                    if c == razn:
                        break
                    else:
                        continue
        print('YES')
        print(' '.join(map(str,ss))) 

    else:
        c = 0
        for i in range(d):
            if c == razn:
                break
            else:
                while ss[i] > s[i][0]:
                    ss[i] = ss[i] - 1
                    c = c + 1
                    if c == razn:
                        break
                    else:
                        continue
        print('YES')
        print(' '.join(map(str,ss)))

