t = int(input())

while t > 0:
    n = int(input())
    s = input()

    history = [a for a in s]
    all_continuous = True
    for ch in history:
        indexes = [i for i, letter in enumerate(s) if letter == ch]
        for i, index in enumerate(indexes):
            if i < len(indexes) - 1:
                if indexes[i + 1] - indexes[i] != 1:
                    all_continuous = False
                    break

    print("YES" if all_continuous else "NO")
    t -= 1
