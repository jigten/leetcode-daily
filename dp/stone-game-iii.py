from functools import lru_cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # @lru_cache(None)
        # def dp(i):
        #     if i >= n:
        #         return 0
        #
        #     res = float("-inf")
        #     take_sum = 0
        #     for k in range(1, 4):
        #         if i + k > n:
        #             break
        #         take_sum += stoneValue[i + k - 1]
        #         res = max(res, take_sum - dp(i + k))
        #
        #     return res

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take_sum = 0
            best = float("-inf")

            for k in range(1, 4):
                if i + k > n:
                    break

                take_sum += stoneValue[i + k - 1]
                best = max(best, take_sum - dp[i + k])

            dp[i] = best

        res = dp[0]
        if res < 0:
            return "Bob"
        elif res == 0:
            return "Tie"
        else:
            return "Alice"
