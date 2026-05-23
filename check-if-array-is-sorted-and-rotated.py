from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        inflection = -1

        if n <= 1:
            return True

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                inflection = i
                break

        if inflection == -1:
            return True

        for i in range(inflection + 1, n):
            if nums[i] < nums[i - 1]:
                return False

        return nums[-1] <= nums[0]
