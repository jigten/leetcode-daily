from typing import List


class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        po, pe = [0] * (n + 1), [0] * (n + 1)

        for i in range(1, n + 1):
            po[i] = po[i - 1]
            pe[i] = pe[i - 1]

            if nums[i - 1] % 2:
                po[i] += 1
            else:
                pe[i] += 1

        S = [0] * (n + 1)

        for i in range(1, n + 1):
            S[i] = b * pe[i] - a * po[i]

        vals = sorted(set(S))
        rank_of = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        bit = [0] * (m + 1)

        def add(i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0

            while i > 0:
                s += bit[i]
                i -= i & -i

            return s

        res = 0

        for q in range(n + 1):
            r = rank_of[S[q]]
            res += q - query(r - 1)
            add(r, 1)

        return res
