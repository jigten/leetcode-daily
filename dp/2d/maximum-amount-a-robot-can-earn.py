from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        val0 = coins[0][0]

        for k in range(3):
            dp[0][0][k] = val0

        if val0 < 0:
            dp[0][0][0] = max(dp[0][0][0], 0)
            dp[0][0][1] = max(dp[0][0][1], 0)
        

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: continue
                curr_coin = coins[r][c]

                for k in range(3):
                    best_prev = float('-inf')
                    if r > 0: best_prev = max(best_prev, dp[r - 1][c][k])
                    if c > 0: best_prev = max(best_prev, dp[r][c - 1][k])

                    dp[r][c][k] = max(dp[r][c][k], best_prev + curr_coin)

                    if curr_coin < 0 and k < 2:
                        best_prev_with_more = float('-inf')
                        if r > 0: best_prev_with_more = max(best_prev_with_more, dp[r - 1][c][k + 1]) 
                        if c > 0: best_prev_with_more = max(best_prev_with_more, dp[r][c- 1][k + 1])

                        dp[r][c][k] = max(dp[r][c][k], best_prev_with_more + 0)

        
        return max(dp[m - 1][n - 1])
        
