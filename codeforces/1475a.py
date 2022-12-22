t = int(input())


def is_odd_divisor(n):
    while n % 2 == 0:
        n //= 2

    if n != 1:
        return "YES"
    else:
        return "NO"


while t > 0:
    n = int(input())
    print(is_odd_divisor(n))

    t -= 1
