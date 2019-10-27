n = int(input())
a = map(int,input().split())
a = list(a)
m = int(input())
b = map(int,input().split())
b = list(b)

c = 0
for i in range(len(a)):
    if c == 1:
        break
    else:
        for j in range(len(b)):
            p = a[i] + b[j]
            if p in a or p in b:
                continue
            else:
                c = c + 1
                print(a[i],b[j])
                break


