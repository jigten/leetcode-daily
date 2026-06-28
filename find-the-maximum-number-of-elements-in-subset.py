from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        one_cnt = counts.get(1, 0)

        res = one_cnt if one_cnt % 2 else one_cnt - 1
        counts.pop(1, None)

        for num in counts:
            x = num
            curr = 0

            while x in counts and counts[x] >= 2:
                curr += 2
                x *= x

            res = max(res, curr)

        return res
