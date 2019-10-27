v = 'ACTG'
def diff(a,b):
    return min((ord(b)-ord(a))%26,(ord(a)-ord(b))%26)

input()
s = input()
print(min([sum([diff(v[j], s[i:i + 4][j]) for j in range(4)]) for i in range(len(s) - 3)]))
      

