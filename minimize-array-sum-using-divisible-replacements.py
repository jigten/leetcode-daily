class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_ = max(nums)
        replacements = [0] * (max_ + 1)
        unique = sorted(list(set(nums)))

        for d in unique:
            for dm in range(d, max_ + 1, d):
                if replacements[dm] == 0:
                    replacements[dm] = d

        res = 0

        for n in nums:
            res += replacements[n]

        return res
