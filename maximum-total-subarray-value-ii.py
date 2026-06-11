import heapq
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # preprocess sparse min and max
        logn = n.bit_length()
        stmin = [[0] * logn for _ in range(n)]
        stmax = [[0] * logn for _ in range(n)]

        for i in range(n):
            stmin[i][0] = stmax[i][0] = nums[i]

        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                stmin[i][j] = min(stmin[i][j - 1], stmin[i + step][j - 1])
                stmax[i][j] = max(stmax[i][j - 1], stmax[i + step][j - 1])

        def queryMax(l, r):
            logn = (r - l + 1).bit_length() - 1
            return max(stmax[l][logn], stmax[r - (1 << logn) + 1][logn])

        def queryMin(l, r):
            logn = (r - l + 1).bit_length() - 1
            return min(stmin[l][logn], stmin[r - (1 << logn) + 1][logn])

        pq = [(-(queryMax(l, n - 1) - queryMin(l, n - 1)), l, n - 1) for l in range(n)]
        heapq.heapify(pq)

        res = 0

        while k:
            negval, l, r = heapq.heappop(pq)
            res -= negval
            k -= 1
            if r > l:
                heapq.heappush(
                    pq, (-(queryMax(l, r - 1) - queryMin(l, r - 1)), l, r - 1)
                )

        return res
