n = int(input())
c = list(map(int, input().split(' ')))

s = 0
d = 0
i = 0
j = n - 1
is_serejas_turn = True
while n > 0:
    if c[i] > c[j]:
        if is_serejas_turn:
            s += c[i]
        else:
            d += c[i]
        i += 1
    else:

        if is_serejas_turn:
            s += c[j]
        else:
            d += c[j]
        j -= 1
    is_serejas_turn = not is_serejas_turn
    n -= 1

print(f'{s} {d}')
