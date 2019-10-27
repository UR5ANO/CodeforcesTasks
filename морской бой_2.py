print('Введите w1 h1 w2 h2')
vvod=input()
w1,h1,w2,h2=vvod.split()
w1=int(w1)
h1=int(h1)
w2=int(w2)
h2=int(h2)

if w1<w2:
    print('Введите правильные данные')
elif w1==w2:
    res=w1+2*h1+2*h2+w2+4
    print(res)
elif w1-w2>1:
    res2=2*w1+2*h1+2*h2+4
    print(res2)
else:
    res1=w1+2*h1+2*h2+w2+5
    print(res1)
    
