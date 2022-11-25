a = list(map(int, input().split(' ')))

c = 0
for i in input():
    c += a[int(i)-1]
print(c)
