from typing import List


class KthLargest:
    k: int
    nums: List[int]
    largest: int
    left: int
    right: int
    sort_done = False

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:

        if not self.sort_done:
            self.nums.append(val)
            self.nums = sorted(self.nums)
            self.sort_done = True
        else:
            if val > self.largest:
                i = 1
            elif val < self.largest:
                pass
            else:
                pass

        self.largest = self.nums[-3]
        self.left = self.nums[-4]
        self.right = self.nums[-2]

        return self.largest


a = [2, 3, 4, 5, 8]

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
