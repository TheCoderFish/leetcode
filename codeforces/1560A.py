t = int(input())


def get_kth_element_in_sequence(k):
    x = 0
    while k != 0:
        x += 1

        if (x % 3 == 0 or x % 10 == 3) and x > 2:
            while x % 3 == 0 or x % 10 == 3:
                x += 1

        k -= 1
    return x


while t > 0:
    t -= 1
    k = int(input())
    print(get_kth_element_in_sequence(k))
