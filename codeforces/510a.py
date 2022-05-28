inputs = input().split(' ')
n, m = [int(i) for i in inputs]

is_end = True

for i in range(n):
    for j in range(m):
        if (i % 2 == 0) or (is_end and (j == m - 1)) or (not is_end and (j == 0)):
            print('#', end='')
        else:
            print('.', end='')
    print('', end='\n')
    if i % 2 != 0:
        is_end = not is_end
