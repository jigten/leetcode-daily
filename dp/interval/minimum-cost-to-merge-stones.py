from typing import List
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix_sums = [0] * (n + 1)

        for i in range(n):
            prefix_sums[i + 1] = stones[i] + prefix_sums[i]

        def getSum(i, j):
            return prefix_sums[j + 1] - prefix_sums[i]

        MAX = float("inf")

        @lru_cache(None)
        def dp(i, j, m):
            # base case: if 1 element, cost 0 to make 1 pile else impossible
            if j == i:
                return 0 if m == 1 else MAX
            # base case: if elements less than m impossible
            if j - i + 1 < m:
                return MAX

            if m == 1:
                return dp(i, j, k) + getSum(i, j)

            ans = MAX

            for mid in range(i, j, k - 1):
                ans = min(ans, dp(i, mid, 1) + dp(mid + 1, j, m - 1))
            return ans

        res = dp(0, n - 1, 1)

        return res
