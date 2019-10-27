n, k = map(int, input().split())
s = input()
s = list(s)

for i in range(n):
	if k == 0:
		break
	replacement = '1' if i == 0 and n > 1 else '0'
	if s[i] == replacement:
		continue
	s[i] = replacement
	k -= 1

print(''.join(s))
