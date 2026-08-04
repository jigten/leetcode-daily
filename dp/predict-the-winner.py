from functools import lru_cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0

            take_left = nums[l] - dfs(l + 1, r)
            take_right = nums[r] - dfs(l, r - 1)

            return max(take_left, take_right)

        return dfs(0, n - 1) >= 0
