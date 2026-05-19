from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= n:
                return 0

            if i == n - 1:
                return nums[-1]

            if i in memo:
                return memo[i]

            best = max(dp(i + 1), dp(i + 2) + nums[i])
            memo[i] = best

            return best

        return dp(0)
