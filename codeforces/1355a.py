t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    if n < 3:
        print(0)
    else:
        print(n - (n // 2) - 1)
