n = int(input())
mw = 0
cw = 0
while n > 0:
    m, c = list(map(int, input().split(' ')))
    if m > c:
        mw += 1
    elif c > m:
        cw += 1
    else:
        pass
    n -= 1

if mw > cw:
    print('Mishka')
elif mw < cw:
    print('Chris')
else:
    print('Friendship is magic!^^')
