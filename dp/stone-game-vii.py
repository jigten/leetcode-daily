from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pref_sum = [0] * (n + 1)

        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                take_i = (pref_sum[j + 1] - pref_sum[i + 1]) - dp[i + 1][j]
                take_j = (pref_sum[j] - pref_sum[i]) - dp[i][j - 1]

                dp[i][j] = max(take_i, take_j)

        return dp[0][n - 1]
