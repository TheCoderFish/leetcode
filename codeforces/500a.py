t = int(input())

while t > 0:
    a, b = list(map(int, input().split(' ')))
    if a > b:
        print(max(a, b + b) ** 2)
    else:
        print(max(b, a+a) ** 2)
    t -= 1
