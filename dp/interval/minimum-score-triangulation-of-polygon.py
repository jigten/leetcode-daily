from typing import List
from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < 3:
                return 0

            if j - i + 1 == 3:
                return values[i] * values[j] * values[j - 1]

            min_score = float('inf')
            for m in range(i + 1, j):
                score = values[i] * values[m] * values[j]
                min_score = min(min_score, dp(i, m) + dp(m, j) + score)

            return min_score

        return dp(0, n - 1)
