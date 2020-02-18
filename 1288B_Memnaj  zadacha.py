t = int(input())

for i in range(t):
    A,B = map(str,input().split())
    a = int(A)

    if B.count('9') == len(B):
        print(a * (len(B)))

    else:
        print(a * (len(B) - 1))
            




