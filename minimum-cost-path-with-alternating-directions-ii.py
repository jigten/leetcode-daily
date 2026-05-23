from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[float('inf')] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                    continue

                entry_cost = (r + 1) * (c + 1)
                wait_cost = 0 if r == m - 1 and c == n - 1 else waitCost[r][c]

                if r > 0:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c])

                if c > 0:
                    dp[r][c] = min(dp[r][c - 1], dp[r][c])

                dp[r][c] += entry_cost + wait_cost

        return dp[m - 1][n - 1]


        # @lru_cache(None)
        # def dp(r, c):
        #     cost = float('inf')
        #     for nr, nc in [(r + 1, c), (r, c + 1)]:
        #         if 0 <= nr < m and 0 <= nc < n:
        #             entry_cost = (nr + 1) * (nc + 1)
        #
        #             if nr == m - 1 and nc == n - 1:
        #                 cost = min(cost, entry_cost)
        #             else:
        #                 cost = min(cost, waitCost[nr][nc] + entry_cost + dp(nr, nc))
        #
        #     return cost 
        #
        # return 1 + dp(0, 0)
