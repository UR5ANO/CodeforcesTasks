t = int(input())
for i in range(t):
    s = input()
    if len(s) < 2:
        print(s[0])
    else:
        s = [int(m) for m in s]
        a = (len(s) - 1) * 9
        b = 0
        q = True
        for j in range(len(s)-1):
            if s[j] > s[j + 1]:
                b = s[j] - 1
                q = False 
                break
            elif s[j] < s[j + 1]:
                b = s[j]
                q = False
                break
            elif s[j] == s[j + 1]:
                continue
    
        if q == True:
            print(a + s[j])
        else:
            print(a + b)
