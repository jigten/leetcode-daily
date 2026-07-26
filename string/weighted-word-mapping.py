from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""

        for w in words:
            w_wt = 0

            for c in w:
                w_wt += weights[ord(c) - ord('a')]

            res += chr(ord('z') - (w_wt % 26))

        return res
