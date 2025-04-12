from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # this will make sure index in j will be of the separator
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # move i to start of the word as word will always start after j
            i = j + 1
            # move j to end of word
            j = i + length

            # get the word
            res.append(s[i:j])

            # set i to end of word to start fresh
            i = j

        return res


input_arr = ['2hi', 'i', 'a#m', 'noor']
encoded = Solution().encode(input_arr)
print(encoded)
decoded = Solution().decode(encoded)
print(decoded)
