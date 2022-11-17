n = int(input())
a = list(map(int, input().split(' ')))


def equalize_welfare(a):
    max_owner = max(a)
    res = 0
    for i in a:
        res += max_owner - i
    print(res)


equalize_welfare(a)
