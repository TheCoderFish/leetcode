t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split(' ')))
    maxa = max(a)
    mina = min(a)
    print(maxa - mina)
    t -= 1
