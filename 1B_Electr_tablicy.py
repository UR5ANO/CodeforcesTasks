n = int(input())
spisok = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(n):
    s = input()
    ss = []
    tek_znach = '0'
    
    for j in s:
        if 63 < ord(j) < 92:        #Определение вида входной строки
            if tek_znach == 'b': 
                continue
            else:
                tek_znach = 'b'
                ss.append('b')
        else:
            if tek_znach == 'c':
                continue 
            else:
                tek_znach = 'c'
                ss.append('c')
            
    if len(ss) == 2:
        spisok_bukv = []                    
        spisok_chisel = []
        for k in s:                     #Решение для входной строки 'bc'
            if 63 < ord(k) < 92:
                spisok_bukv.append(k)
            else:
                spisok_chisel.append(k) 

        spisok_bukv.reverse()
        res = 0
        for m in range(len(spisok_bukv)):
            res = res + (spisok.index(spisok_bukv[m]) + 1) * (26 ** m)

        res = str(res)
        print('R' + ("".join(spisok_chisel)) + 'C' + res)

    else:
        stroka = []                     #Решение для входной строки 'bcbc'
        stolbec = []
        counter = 0
        for g in s:                     
            if 47 < ord(g) < 60:
                if counter == 1:
                    stroka.append(g)
                else:
                    stolbec.append(g)
            else:
                counter = counter + 1
        a = int("".join(stolbec))
        ans = []
        while a > 0:
            ost = a % 26
            if ost == 0:
                ost = 26
            ans.append(ost)
            a = a - ost
            a //= 26
        ans = reversed(ans)
        # print(ans)
        ans = [chr(ord('A') + c-1) for c in ans]
                
        print("".join(ans) + "".join(stroka))



