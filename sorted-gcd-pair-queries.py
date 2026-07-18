import bisect
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        exact_gcds = [0] * (max_val + 1)

        for i in range(max_val, 0, -1):
            count_multiples = 0
            for j in range(i, max_val + 1, i):
                count_multiples += freq[j]

            total_pairs = (count_multiples * (count_multiples - 1)) // 2

            minus_pairs = 0
            for j in range(2 * i, max_val + 1, i):
                minus_pairs += exact_gcds[j]

            exact_gcds[i] = total_pairs - minus_pairs

        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_gcds[i]

        res = []
        for q in queries:
            idx = bisect.bisect_right(exact_gcds, q)
            res.append(idx)

        return res
