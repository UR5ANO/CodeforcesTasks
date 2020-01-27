q = int(input())
for i in range(q):
    s = input()

    du = min(s.count('D'),s.count('U'))
    lr = min(s.count('L'),s.count('R'))

    if du != 0 and lr != 0:
        print(2 * du + 2 * lr)
        print('D' * du + 'L' * lr + 'U' * du + 'R' * lr)

    elif du == 0:
        if s.count('L') != 0 and s.count('R') != 0:
            print(2)
            print('LR')
        else:
            print(0)

    elif lr == 0:
        if s.count('D') != 0 and s.count('U') != 0:
            print(2)
            print('DU')
        else:
            print(0)
