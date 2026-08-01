from functools import lru_cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r):
            return 0

        return dfs(0, n - 1) >= 0
