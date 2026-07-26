import bisect
from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def helper(ast: List[int], ad: List[int], bst: List[int], bd: List[int]) -> int:
            n = len(bst)
            combined = sorted(zip(bst, bd))
            sorted_starts = [x[0] for x in combined]
            sorted_durations = [x[1] for x in combined]

            pre_min = [0] * n
            pre_min[0] = sorted_durations[0]
            for i in range(1, n):
                pre_min[i] = min(pre_min[i - 1], sorted_durations[i])

            post_min = [0] * n
            post_min[-1] = sorted_starts[-1] + sorted_durations[-1]

            for i in range(n - 2, -1, -1):
                post_min[i] = min(post_min[i + 1], sorted_starts[i] + sorted_durations[i])

            res = 10**9

            for st, d in zip(ast, ad):
                et = st + d
                idx = bisect.bisect_right(sorted_starts, et)

                if idx < n:
                    res = min(res, post_min[idx])

                if idx > 0:
                    res = min(res, et + pre_min[idx - 1])

            return res

        return min(
            helper(landStartTime, landDuration, waterStartTime, waterDuration),
            helper(waterStartTime, waterDuration, landStartTime, landDuration),
        )
