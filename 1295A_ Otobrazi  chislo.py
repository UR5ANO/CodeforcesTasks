t = int(input())

for i in range(t):
    n = int(input())

    if n % 2 == 0:
        ed = n // 2
        sem = 0
    else:
        ed = n // 2 - 1
        sem = 1

    print('7' * sem + '1' * ed)
     

