T = int(input())

for i in range(T):
    a,b,n = map(int,input().split())
    print([a, b, a ^ b][n % 3])


