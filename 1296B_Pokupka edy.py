t = int(input())

for i in range(t):
    n = int(input())

    res = (n // 10) * 10
    ost = n % 10 + n // 10
    
    while ost > 9:
        res += (ost // 10) * 10
        ost = ost % 10 + ost // 10  

    print(res + ost)
