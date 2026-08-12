from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = nums[i] + pre[i]

        seq_pre_sum = nums[0]

        for r in range(1, n):
            if nums[r] == nums[r - 1] + 1:
                seq_pre_sum = max(seq_pre_sum, pre[r + 1] - pre[0])
            else:
                break

        seen = set(nums)

        while seq_pre_sum in seen:
            seq_pre_sum += 1

        return seq_pre_sum
