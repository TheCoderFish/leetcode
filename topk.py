from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        return list(sorted(count, key=lambda x: count[x], reverse=True))[:k]


nums = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4]

print(Solution().topKFrequent(nums, k=1))
