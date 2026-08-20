from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sum_ = sum(nums)
        remainder = sum_ % p

        if remainder % p == 0:
            return 0

        pref = 0
        res = n
        seen = {0: -1}

        for i, num in enumerate(nums):
            pref += num
            mod = pref % p
            target_mod = (mod - remainder + p) % p
            if target_mod in seen:
                res = min(res, i - seen[target_mod])

            seen[mod] = i

        return res if res != n else -1
