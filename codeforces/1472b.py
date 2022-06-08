t = int(input())


def is_fair_division_possible(candies):
    total_weight = sum(candies)

    if total_weight % 2 != 0:
        return "NO"

    number_of_one = len(list(filter(lambda x: x == 1, candies)))

    if number_of_one >= 2:
        return "YES"

    if number_of_one == 0:
        ans = "YES" if len(candies) % 2 == 0 else "NO"
        return ans


while t > 0:
    n = int(input())
    candies = list(map(int, input().split()))
    print(is_fair_division_possible(candies))
    t -= 1
