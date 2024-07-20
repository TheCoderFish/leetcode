class Solution(object):
    solved = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        if n == 0:
            return 1
        n1 = self.solved[n - 1] if (n - 1) in self.solved else self.climbStairs(n - 1)
        n2 = self.solved[n - 2] if (n - 2) in self.solved else self.climbStairs(n - 2)

        self.solved[n-1] = n1
        self.solved[n-2] = n2

        return n1 + n2


print(Solution().climbStairs(38))
