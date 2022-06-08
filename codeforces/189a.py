entries = input()
n, a, b, c = [int(i) for i in entries.split(' ')]

dp = {}


def get_max_pieces(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -9999999

    if n in dp:
        return dp[n]
    dp[n] = 1 + max(get_max_pieces(n - a, a, b, c), get_max_pieces(n - b, a, b, c),
                    get_max_pieces(n - c, a, b, c))
    return dp[n]


print(get_max_pieces(n, a, b, c))