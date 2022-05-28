t = int(input())

while t > 0:
    n = list(input())
    n.reverse()

    result = ''
    count = 0
    for idx, digit in enumerate(n):
        res = int(digit) * (10 ** idx)
        if res > 0:
            result += str(res) + ' '
            count += 1
    print(count)
    print(result)
    t -= 1
