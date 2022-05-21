def binary_search_v2(arr, l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
        return -1


def main():
    arr = [1, 2, 3, 4, 5]
    target = 5
    print(binary_search_v2(arr, 0, len(arr) - 1, target))


if __name__ == "__main__":
    main()
