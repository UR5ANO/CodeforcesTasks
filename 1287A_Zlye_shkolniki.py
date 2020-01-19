t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    s = list(s)

    if len(s) == 1:
        print(0)
    else:
        c = 0
        i = 0
        while i < len(s):
            if s[i] == 'P':
                c = c + 1
            else:
                break
            i = i + 1

        s[:c] = []
        
        if len(s) <= 1:
            print(0)
        else:
            ss = []
            per = 0
            for i in range(len(s)):
                if s[i] == 'A':
                    ss.append(per)
                    per = 0
                elif s[i] == 'P':
                    per = per + 1
                    
            ss.append(per)
            print(max(ss))
