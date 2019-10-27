def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True   

n = int(input())
s = list(map(int,input().split()))

ss = [s]
while len(ss):
  print("ss в начале итерации: {}".format(ss))
  a = ss.pop(0)
  print("Достали из ss: {}".format(a))
  if is_sorted(a):
    print(len(a))
    break
  l = a[:len(a) // 2]
  r = a[len(a) // 2:]
  print("Ложим в a: {}".format(l))
  ss.append(l)
  print("Ложим в a: {}".format(r))
  ss.append(r)
