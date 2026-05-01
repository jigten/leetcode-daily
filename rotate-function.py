from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # compute initial k = 0
        f = sum(i * n for i, n in enumerate(nums))
        res = f

        # perform upto n rotation functions
        # we can see that every rotation will increase every n upto n - 1 by 1x (essentially add total_sum)
        # the last element is dropped therefore we need to remove n copies of it (i.e. multiplier + 1 from total_sum)
        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            res = max(res, f)

        return res

solution = Solution()
assert(solution.maxRotateFunction(nums = [4,3,2,6]) == 26)
assert(solution.maxRotateFunction(nums = [100]) == 0)


