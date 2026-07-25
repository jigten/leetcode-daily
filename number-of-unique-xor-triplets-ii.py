from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        limit = max(nums) * 2
        has_pair = [False] * limit

        for a in nums:
            for b in nums:
                has_pair[a ^ b] = True

        seen = [False] * limit

        for i, has in enumerate(has_pair):
            if has:
                for n in nums:
                    seen[n ^ i] = True

        return sum(seen)

        unique_nums = set(nums)
        unique_list = list(unique_nums)

        xors = set()

        m = len(unique_list)

        for i in range(m):
            for j in range(i + 1, m):
                xors.add(unique_list[i] ^ unique_list[j])

        if len(nums) > len(unique_nums):
            xors.add(0)

        seen = set()

        for x in unique_list:
            for xor in xors:
                seen.add(x ^ xor)

        return len(seen)
