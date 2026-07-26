from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])

                if c > 0:
                    dp[r][c] = min(dp[r][c], dp[r][c - 1] + grid[r][c])

        return dp[rows - 1][cols - 1]

        # memo = {}
        # def dp(r, c):
        #     if r == rows - 1 and c == cols - 1:
        #         return grid[r][c]
        #
        #     if (r, c) in memo:
        #         return memo[(r, c)]
        #
        #     res = float('inf')
        #     for dr, dc in [(r + 1, c), (r, c + 1)]:
        #         if 0 <= dr < rows and 0 <= dc < cols:
        #             res = min(res, dp(dr, dc) + grid[r][c])
        #
        #     memo[(r, c)] = res
        #     return res
        #
        # return dp(0, 0)
