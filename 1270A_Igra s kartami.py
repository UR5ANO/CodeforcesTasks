t = int(input())
for i in range(t):
    n,k1,k2 = map(int,input().split())
    spisok_k1 = map(int,input().split())
    spisok_k1 = list(spisok_k1)
    spisok_k2 = map(int,input().split())
    spisok_k2 = list(spisok_k2)

    if max(spisok_k1) > max(spisok_k2):
        print('Yes')
    else:
        print('No')
