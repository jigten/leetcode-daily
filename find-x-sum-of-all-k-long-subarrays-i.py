from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(subarr):
            counts = Counter(subarr)
            topx = sorted(
                [(n, c) for n, c in counts.items()],
                key=lambda e: (e[1], e[0]),
                reverse=True,
            )[:x]
            return sum(n * c for n, c in topx)

        res = []
        for i in range(len(nums) - k + 1):
            res.append(xsum(nums[i : i + k]))

        return res
