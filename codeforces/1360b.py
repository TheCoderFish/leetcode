t = int(input())
while t > 0:
    n = int(input())
    s = list(map(int, input().split(' ')))
    s.sort()
    min = 1000
    for i, si in enumerate(s):
        if i < n-1 and abs(s[i] - s[i + 1]) < min:
            min = abs(s[i] - s[i + 1])
    print(min)

    t -= 1
