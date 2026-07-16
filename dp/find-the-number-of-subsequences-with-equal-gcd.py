import math
from functools import lru_cache
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)

        # iterative solution
        curr_dp = [[0] * 201 for _ in range(201)]
        next_dp = [[0] * 201 for _ in range(201)]

        # base case
        for g1 in range(201):
            for g2 in range(201):
                if g1 > 0 and g1 == g2:
                    next_dp[g1][g2] = 1

        for i in range(n - 1, -1, -1):
            curr = nums[i]
            for g1 in range(201):
                for g2 in range(201):
                    take1 = next_dp[math.gcd(g1, curr)][g2]
                    take2 = next_dp[g1][math.gcd(g2, curr)]
                    skip = next_dp[g1][g2]

                    curr_dp[g1][g2] = (take1 + take2 + skip) % (10**9 + 7)

            next_dp = curr_dp
            curr_dp = [[0] * 201 for _ in range(201)]

        return next_dp[0][0]

        # recursive solution
        @lru_cache(None)
        def dp(i, gcd1, gcd2):
            if i == n:
                return 1 if (gcd1 == gcd2 and gcd1 > 0 and gcd2 > 0) else 0

            cnt = 0
            curr = nums[i]

            cnt += dp(i + 1, math.gcd(gcd1, curr), gcd2)
            cnt += dp(i + 1, gcd1, math.gcd(gcd2, curr))
            cnt += dp(i + 1, gcd1, gcd2)

            return cnt

        return dp(0, 0, 0) % (10**9 + 7)
