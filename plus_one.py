from typing import List

[9]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = False
        res = []

        for idx, num in enumerate(digits):
            if idx == 0:
                if num == 9:
                    carry = True
                    res.append(0)
                else:
                    res.append(num + 1)


            else:
                if carry:
                    if num == 9:
                        res.append(0)
                    else:
                        res.append(num + 1)
                        carry = False
                else:
                    res.append(num)

        if carry:
            res.append(1)

        res.reverse()
        return res


print(Solution().plusOne([1]))
print(Solution().plusOne([1, 9]))
print(Solution().plusOne([9, 9, 9, 9]))
print(Solution().plusOne([9, 0, 9, 9]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([1, 2, 3]))
