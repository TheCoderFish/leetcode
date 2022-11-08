numbers = list(map(int, input().split(' ')))
numbers.sort()

print(f'{numbers[3] - numbers[0]} {numbers[3] - numbers[1]} {numbers[3] - numbers[2]}')
