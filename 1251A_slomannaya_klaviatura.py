n = int(input())

for _ in range(n):
    s = input()
    good_letters = set()
    current_letter = '0'
    counter = 0

    s = s + '0'
    for l in s:
        if l == current_letter:
            counter += 1
        else:
            if counter % 2 != 0:
                good_letters.add(current_letter)
            current_letter = l
            counter = 1

    print(''.join(sorted(good_letters)))
