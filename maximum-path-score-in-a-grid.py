from typing import List
from functools import cache

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        NEG = -10**9

        prev_dp = [[NEG] * (k + 1) for _ in range(cols)]

        for r in range(rows):
            curr_row = [[NEG] * (k + 1) for _ in range(cols)]

            for c in range(cols):
                curr_score = grid[r][c]
                curr_cost = 1 if curr_score > 0 else 0

                if r == 0 and c == 0:
                    if curr_cost <= k:
                        curr_row[0][curr_cost] = curr_score
                    continue

                for ki in range(curr_cost, k + 1):
                    best = NEG

                    if r > 0 and prev_dp[c][ki - curr_cost] != NEG:
                        best = max(best, prev_dp[c][ki - curr_cost] + curr_score)

                    if c > 0 and curr_row[c - 1][ki - curr_cost] != NEG:
                        best = max(best, curr_row[c - 1][ki - curr_cost] + curr_score)

                    curr_row[c][ki] = best

            prev_dp = curr_row

        ans = max(prev_dp[cols - 1])
        return -1 if ans < 0 else ans

        @cache
        def dp(r, c, cost):
            if cost > k:
                return float('-inf')

            if r == rows - 1 and c == cols - 1:
                return grid[r][c]

            best_score = float('-inf')

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    add_cost = 1 if grid[nr][nc] > 0 else 0
                    next_cost = cost + add_cost
                    if next_cost > k: continue
                    best_score = max(best_score, dp(nr, nc, next_cost))
            
            return best_score + grid[r][c]

        inital_cost = 1 if grid[0][0] > 0 else 0
        res = dp(0, 0, inital_cost)

        return -1 if res == float('-inf') else res

solution = Solution()
assert(solution.maxPathScore(grid = [[0, 1],[2, 0]], k = 1) == 2)
assert(solution.maxPathScore(grid = [[0, 1],[1, 2]], k = 1) == -1)
