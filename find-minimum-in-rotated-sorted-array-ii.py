from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            mval = nums[r]

            if mval < nums[r]:
                res = min(mval, res)
                r = m - 1
            elif mval > nums[r]:
                l = m + 1
            else:
                res = min(res, mval)
                r -= 1

        return res
