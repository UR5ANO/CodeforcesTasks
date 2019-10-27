print('Морской бой')
w1=int(input('Ширина первого корабля:'  ))
h1=int(input('Высота первого корабля:'  ))
w2=int(input('Ширина второго корабля:'  ))
h2=int(input('Высота второго корабля:'  ))

if w1<w2:
    print('Введите правильные данные')
elif w1==w2:
    res=w1+2*h1+2*h2+w2+4
    print(res)
else:
    res1=w1+2*h1+2*h2+w2+5
    print(res1)
    
