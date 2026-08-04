class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        res = 1

        while word * (res + 1) in sequence:
            res += 1

        return res
