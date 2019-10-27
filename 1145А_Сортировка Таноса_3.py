def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def thanos_sort(a):
    if is_sorted(a):
        return len(a)
    left_result = thanos_sort(a[:len(a) // 2])
    right_result = thanos_sort(a[len(a) // 2:])
    return max(left_result, right_result)
    

n = int(input())
s = list(map(int,input().split()))

print(thanos_sort(s))
