from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        leftSum, rightSum = 0, sum(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            res.append(abs(leftSum - rightSum))
            leftSum += nums[i]

        return res
