class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        post_mins = [float("inf")] * (n + 1)

        for i in range(n - 1, -1, -1):
            post_mins[i] = min(post_mins[i + 1], nums[i])

        print(post_mins)

        res = float("inf")
        pre_max = nums[0]

        for i in range(n):
            pre_max = max(pre_max, nums[i])

            if pre_max - post_mins[i] <= k:
                res = min(res, i)

        return -1 if res == float("inf") else res
