import bisect
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = list(
            sorted(
                [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
                key=lambda x: x[1],
            )
        )
        ends = [r for (l, r, w, i) in arr]
        n = len(arr)

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, oi = arr[i - 1]
            p = bisect.bisect_left(ends, l)
            for k in range(1, 5):
                skip = dp[i - 1][k]
                base = dp[p][k - 1]
                take = (w + base[0], sorted(base[1] + [oi]))
                dp[i][k] = better(skip, take)

        return dp[n][4][1]
