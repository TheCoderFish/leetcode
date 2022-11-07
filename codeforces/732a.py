# k - cost of shovel
# r - one coin

k, r = map(int, input().split())

t = k
n = 0
while not (t % 10 == 0 or t % 10 == r):
    n += 1
    t += k

print(n + 1)
