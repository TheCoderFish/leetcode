t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split(' ')))
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count:
        if count[i] == 1:
            print(a.index(i) + 1)

    t -= 1
