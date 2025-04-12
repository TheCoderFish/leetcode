from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('|') if s else []


input_arr = ['']
encoded = Solution().encode(input_arr)
decoded = Solution().decode(encoded)
print(decoded)
