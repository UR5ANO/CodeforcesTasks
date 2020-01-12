n,v = map(int,input().split())
ba = []
ka = []
t = int(input())
for i in range(t):
    hh,mm = map(int,input().split())
    otvet = 1440 - (hh * 60 + mm)
    print(otvet)
