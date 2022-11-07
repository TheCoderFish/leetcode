# n - dragons
# s - kiritos strength
# i -> nth dragon
# xi -> xth dragons strength
# yi -> bonus strength of ith dragon

defeat_all = True
s, n = map(int, input().split())
a = [(list(map(int, input().split()))) for _ in range(n)]
for x, y in sorted(a):
    if s > x:
        s += y
    else:
        defeat_all = False
        break

print('YES' if defeat_all else 'NO')
