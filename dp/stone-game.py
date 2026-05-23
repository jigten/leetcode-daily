from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0

            pick_left = piles[l] - dp(l + 1, r)
            pick_right = piles[r] - dp(l, r - 1)

            return max(pick_left, pick_right)

        return dp(0, n - 1) > 0
