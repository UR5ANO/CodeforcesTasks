n = int(input())
s = map(int,input().split())
s = list(s)
import math
chet = 0
nechet = 0
posled = 1
perv = None
for i in range(len(s)):         #Определение заданных четных и нечетных
    if s[i] == 0:          # и формирование списка из 0,1,2 
        continue
    elif s[i] % 2 == 0:
        chet = chet + 1
        posled = 2
        if perv is None:
            perv = 2
        s[i] = 2
    else:
        nechet = nechet + 1
        posled = 1
        if perv is None:
            perv = 1
        s[i] = 1

chet = len(s)//2 - chet                  #Количество оставшихся четных и нечетных 
nechet = math.ceil(len(s)/2) - nechet


otvet = 0                    # Определение ответа  
for i in range(len(s)-1):
    if s[i] != s[i+1] and s[i] > 0 and s[i+1] > 0:
        otvet = otvet + 1
        
s = [3] + s + [3]

# (5,8,1,2)

ss = []
l = None
for i in range(len(s)):
    if l is None:
        l = i
    elif s[i] != 0:
        if i - l > 1:
            ss.append((l+1,i-1,s[l],s[i]))
        l = i

def por(k):
    f = 2
    if k[2] == 3 or k[3] == 3:
        f = 1
    elif k[2] == k[3]:
        f = 0
    d = k[1] - k[0] + 1
    return (f,d)

ss.sort(key=por)

d = {
    1: nechet,
    2: chet,
}
for k in ss:
    if k[2] == 3 and k[3] == 3:
        if k[1] - k[0] + 1 > 1:
            otvet = otvet + 1
    
    elif k[2] == k[3]:
        if d[k[2]] >= k[1] - k[0] + 1:
            d[k[2]] -= k[1] - k[0] + 1

        else:
            otvet = otvet + 2

    elif k[2] == 3:
        if d[k[3]] >= k[1] - k[0] + 1:
            d[k[3]] -= k[1] - k[0] + 1

        else:
            otvet = otvet + 1

    elif k[3] == 3:
        if d[k[2]] >= k[1] - k[0] + 1:
            d[k[2]] -= k[1] - k[0] + 1

        else:
            otvet = otvet + 1

    else:
        otvet = otvet + 1

     
print(otvet)

