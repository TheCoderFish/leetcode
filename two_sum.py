class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}

        for idx, n in enumerate(nums):
            rem = target - n
            if target - n in hash:
                return [hash[rem], idx]
            else:
                hash[n] = idx
