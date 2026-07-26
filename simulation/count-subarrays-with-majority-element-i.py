from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1

                if cnt * 2 > (j - i + 1):
                    res += 1

        return res
