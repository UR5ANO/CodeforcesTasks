n = int(input())
for j in range(n):
    s = input()
    s = list(s)
    s.sort()

    a = 'Yes'
    for i in range(len(s)-1):
        if ord(s[i]) - ord(s[i+1]) != -1:
            a = 'No'
            break

    print(a)

