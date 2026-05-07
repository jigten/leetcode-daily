from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = [float("-inf")] * n
        res = [0] * n

        curr_max = float("-inf")
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            pre_max[i] = curr_max

        post_min = nums[-1]
        res[-1] = pre_max[-1]

        for i in range(n - 2, -1, -1):
            if pre_max[i] > post_min:
                res[i] = res[i + 1]
            else:
                res[i] = pre_max[i]

            post_min = min(post_min, nums[i])

        return res


solution = Solution()
assert solution.maxValue([2, 1, 3]) == [2, 2, 3]
assert solution.maxValue([2, 3, 1]) == [3, 3, 3]
