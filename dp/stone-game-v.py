from functools import lru_cache
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = stoneValue[i] + pref[i]

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0

            maxScore = 0
            for k in range(i, j):
                leftSum = pref[k + 1] - pref[i]
                rightSum = pref[j + 1] - pref[k + 1]

                if leftSum < rightSum:
                    maxScore = max(maxScore, leftSum + dp(i, k))
                elif leftSum > rightSum:
                    maxScore = max(maxScore, rightSum + dp(k + 1, j))
                else:
                    maxScore = max(maxScore, leftSum + max(dp(i, k), dp(k + 1, j)))

            return maxScore

        return dp(0, n - 1)
