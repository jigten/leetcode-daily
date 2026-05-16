from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            mval = nums[m]

            if mval <= nums[-1]:
                res = mval
                r = m - 1
            elif mval > nums[-1]:
                l = m + 1
        return res
