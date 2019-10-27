n = int(input())

s = {}
name = []
ball = []
for i in range(n):
    a,c = input().split()
    c = int(c)
    name.append(a)
    ball.append(c)
    
    s[a] = s.get(a,0) + c

score = max(s.values())

winners = {}
for k, v in s.items(): # k = "mike", v = 5
    if v == score:
        winners[k] = 0
        
winner = None
for n, b in zip(name, ball):
    if n in winners:
        winners[n] += b
        if winners[n] >= score:
            winner = n
            break

print(winner)
