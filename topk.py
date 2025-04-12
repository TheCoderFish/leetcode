import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=lambda n: count[n])


nums = [1, 1, 1, 3, 3, 3, 2, 2, 2,2]

print(Solution().topKFrequent(nums, k=2))
