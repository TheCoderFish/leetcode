import math


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        total_sum = 0
        result = False
        mem = set()

        while total_sum != 1:
            digits = list(str(n))
            total_sum = int(sum(map(lambda x: math.pow(int(x), 2), digits)))

            if n in mem:
                break
            else:
                if total_sum != 1:
                    mem.add(n)
                    n = str(total_sum)
                else:
                    result = True

        return result


print(Solution().isHappy(34672823))
print(Solution().isHappy(2))
