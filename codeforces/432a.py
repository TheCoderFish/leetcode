n, k = map(int, input().split(' '))
y = list(filter(lambda x: 5 - x >= k, map(int, input().split(' '))))
print(len(y) // 3)
