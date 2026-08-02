from typing import List


class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            x, y = 0, 0
            for j in range(i, n):
                if nums[j] % 2:
                    y += 1
                else:
                    x += 1

                if (x / y) <= (a / b):
                    res += 1

        return res
