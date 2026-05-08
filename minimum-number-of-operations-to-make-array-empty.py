from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        counts = Counter(nums)

        for cnt in counts.values():
            if cnt == 1:
                return -1

            res += ceil(cnt / 3)

        return res
