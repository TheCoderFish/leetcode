t = int(input())
while t > 0:
    b = input()
    a = [b[i:i + 2] for i in range(0, len(b), 2)]
    c = ''
    for i in range(0, len(a) - 1):
        c += a[i][0]
    c += a[len(a) - 1]

    print(c)
    t -= 1
