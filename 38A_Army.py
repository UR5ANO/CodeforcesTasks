n = int(input())
leta = map(int,input().split())
leta = list(leta)
zvanie_min,zvanie_max = map(int,input().split())

leta = leta[zvanie_min-1:zvanie_max-1]
print(sum(leta))

