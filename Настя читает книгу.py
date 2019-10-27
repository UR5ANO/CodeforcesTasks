def chisla():
    p = input().split(' ')
    return int(p[0]), int(p[1])

def linear_search(s, k):
    for i in range(len(s)):
        if s[i] == k:
            return i

def cmp_int(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1    

def cmp_list(elem, value):
    if elem[0] <= value <= elem[1]:
        return 0
    elif elem[1] < k:
        return -1
    else:
        return 1    


def binary_search(s, k, cmp):
    l, r = 0, len(s)-1
    while l <= r:
        m = (l + r) // 2
        if cmp(s[m], k) == 0:
            return m
        elif cmp(s[m], k) == -1:
            l = m + 1
        else:
            r = m - 1

n = int(input())
s = []

for i in range(n):
    r, t = chisla()
    s.append([r, t])

k = int(input())


i = binary_search(s, k, cmp_list)
print(n-i)

print(binary_search([1, 3, 8, 11, 15, 19, 21], 15, cmp_int))


