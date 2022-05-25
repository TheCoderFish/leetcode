n = int(input())

entries = input()
parsed_entries = [int(i) for i in entries.split(' ')]


def get_untreated_crimes(entries):
    officers = 0
    crimes = 0
    for i in entries:
        if i != -1:
            officers += i
        else:
            if officers == 0:
                crimes += 1
            else:
                officers -= 1

    return crimes


print(get_untreated_crimes(parsed_entries))
