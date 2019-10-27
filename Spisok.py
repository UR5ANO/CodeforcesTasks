print('Открываем список')
f = open ('Spisok.txt','r')
l = f.read()
print(l)
l = l.split('\n')
f.close()
print(l) 

while True:
    s = input()
    
    if s[0] == '+':
        if s[1:] in l:
            print('Этот человек уже есть в списке')
        else:
            l.append(s[1:])
            print('{} добавлен в список'.format(s[1:]))
    elif s[0] == '-':
        if s[1:] in l:
            ll = []
            print(ll)
            for i in l:
                if i != s[1:]:
                    ll.append(i)
            l = ll
            print('{} удален из списка'.format(s[1:]))
        else:
            print('Такого человека нет в списке')

    elif s == '=':
        print(l.sorted())

    elif s == 'exit':
        print('Закрываем программу')
        break
    else:
        print('Неправильный ввод')
        
    
f = open ('Spisok.txt','w')
print(l)
l = '\n'.join(l)
print(l)
f.write(l)
f.close()

print('Закрываем список')
