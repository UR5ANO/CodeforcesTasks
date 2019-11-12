Q = int(input())

for i in range(Q):
    n = int(input())
    nechet = []
    chet_ploh = []
    for j in range(n):
        s = input()
        s = list(s)
             
        if len(s) % 2 != 0:
            nechet.append(1)
        else:
            if s.count('0') % 2 != 0 and s.count('1') % 2 != 0:
                chet_ploh.append(1)
    
    if len(nechet) > 0:
        print(n)
    else:
        if len(chet_ploh) % 2 != 0:
            print(n-1)
        else:
            print(n)
            
