max_powers = [0, 1, 2, 3]


def get_boring_series(start, stop_number):
    series = []
    sum = 0
    for i in max_powers:
        generated = (start * 10 ** i)

        series.append(generated + sum)
        if stop_number == generated + sum:
            return series
        sum += generated

    return series


def get_keypress_count(stop_number):
    all = []
    for i in range(1, 10):
        series = get_boring_series(i, stop_number)
        all.extend(series)
        if stop_number in series:
            break

    answer = 0
    for x in all:
        answer += count_number_of_digits(x)
    return answer


def count_number_of_digits(number):
    return len(list(str(number)))


t = int(input())

while t > 0:
    t -= 1
    k = int(input())
    print(get_keypress_count(k))
