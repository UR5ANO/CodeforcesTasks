t = int(input())
for i in range(t):
    R,G,B = map(int,input().split())

    if R == max(R,G,B):
        if G + B >= R - 1:
            print('Yes')
        else:
            print('No')

    elif G == max(R,G,B):
        if R + B >= G - 1:
            print('Yes')
        else:
            print('No')

    elif B == max(R,G,B):
        if R + G >= B - 1:
            print('Yes')
        else:
            print('No')

    else:
        print('Yes')
