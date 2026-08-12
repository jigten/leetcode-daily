from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = piles[i] + pre[i]

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            res = -(10**9)
            for x in range(1, min(n - i, 2 * M) + 1):
                j = i + x
                taken = pre[j] - pre[i]
                opp = dp(j, max(M, x))
                res = max(res, taken + pre[n] - pre[j] - opp)

            return res

        return dp(0, 1)
