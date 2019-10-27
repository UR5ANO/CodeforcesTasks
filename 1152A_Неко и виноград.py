vvod = input()
n,m = vvod.split()
sn = map(int,input().split(' '))
sm = map(int,input().split(' '))
sn = list(sn)
sm = list(sm)

nechet_sn = 0
chet_sn = 0
for a in sn:
    if a%2 !=0:
        nechet_sn = nechet_sn + 1

    else:
        chet_sn = chet_sn + 1

nechet_sm = 0
chet_sm = 0
        
for b in sm:
    if b%2 !=0:
        nechet_sm = nechet_sm + 1
    
    else:
        chet_sm = chet_sm + 1 

if chet_sn <= nechet_sm:
    p = chet_sn
else:
    p = nechet_sm

if nechet_sn <= chet_sm:
    k = nechet_sn
else:
    k = chet_sm

    
print(p + k)
    

