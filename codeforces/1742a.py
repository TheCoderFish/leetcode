t = int(input())
while t > 0:
    inputs = list(map(int, input().split(' ')))
    inputs.sort()
    if inputs[0]+inputs[1]== inputs[2]:
        print("YES")
    else:
        print("NO")
    t -= 1
