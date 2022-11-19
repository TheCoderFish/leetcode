n = int(input())

if n > -1:
    print(n)
else:
    s = [str(d) for d in str(n)]
    l = len(s)
    a = s.copy()
    b = s.copy()
    a = s[:l - 1]
    b = s[:l - 2] + s[l - 1:]
    if int(''.join(a)) > int(''.join(b)):
        print(int(''.join(a)))
    else:
        print(int(''.join(b)))
