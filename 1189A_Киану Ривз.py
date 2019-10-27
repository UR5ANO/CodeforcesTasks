n = int(input())
s = input()

if s.count('1') != s.count('0'):
    print('1')
    print(s)
else:
    k = 1
    for i in range(n):
        k = k + 1
        s1 = s[0:i+1]
        s2 = s[i+1:]
        
        if s1.count('1') != s1.count('0') and s2.count('1') != s2.count('0'):
            print(k)
            print("".join(s1),"".join(s2))
            break
    
    
        
 

