from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = stones[i] + pref[i]

        dp = [0] * (n + 1)
        best = pref[n]

        for i in range(n - 1, 0, -1):
            dp[i] = best
            best = max(best, pref[i] - dp[i])
