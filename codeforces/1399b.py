t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    mina = min(a)
    minb = min(b)

    moves = 0

    for i in range(n):
        moves += max(a[i] - mina, b[i] - minb)
    print(moves)
    t -= 1
