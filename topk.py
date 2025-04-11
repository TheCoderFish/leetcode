import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []

        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        return [num for freq, num in heap]


nums = [2, 2, 2, 1, 1, 1, 3, 4, 4, 4]

print(Solution().topKFrequent(nums, k=2))
