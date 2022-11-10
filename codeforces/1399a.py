t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split(' ')))
    a.sort()

    is_possible = True
    for i in range(n - 1):
        if abs(a[i + 1] - a[i]) <= 1:
            continue
        else:
            is_possible = False
            break

    print('YES' if is_possible else 'NO')
    t -= 1
