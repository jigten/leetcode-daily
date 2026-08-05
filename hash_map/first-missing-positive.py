from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # o(1) space
        n, i = len(nums), 0
        res = 1

        while i < n:
            curr = nums[i] - 1

            if curr != i and 0 <= curr < n and nums[curr] != curr + 1:
                nums[i], nums[curr] = nums[curr], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != res:
                return res
            res += 1

        return res

        # o(n) space
        seen = set(nums)
        mx = max(nums)

        if mx <= 0:
            return 1

        for i in range(1, mx + 1):
            if i not in seen:
                return i
        return mx + 1
