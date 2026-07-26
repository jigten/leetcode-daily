import math
from typing import List


class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        max_ = prefixGcd[0] = nums[0]

        for i in range(1, n):
            max_ = max(nums[i], max_)
            prefixGcd[i] = math.gcd(max_, nums[i])

        res = 0
        prefixGcd.sort()
        for i in range(n // 2):
            res += math.gcd(prefixGcd[i] + prefixGcd[n - i - 1])

        return res
