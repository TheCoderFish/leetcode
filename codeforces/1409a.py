t = int(input())

while t > 0:
    c = 0

    a, b = map(int, input().split(' '))

    diff = abs(a - b)

    while diff != 0:
        if diff > 10:
            times10 = diff // 10
            c += times10
            diff = diff % 10
        else:
            diff = 0
            c += 1

    print(c)
    t -= 1
