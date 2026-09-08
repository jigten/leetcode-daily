from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        odd_pre, even_pre = 0, 0
        odd_post, even_post = [0] * (n + 1), [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            if i % 2:
                odd_post[i] = odd_post[i + 1] + nums[i]
                even_post[i] = even_post[i + 1]
            else:
                even_post[i] = even_post[i + 1] + nums[i]
                odd_post[i] = odd_post[i + 1]

        for i in range(n):
            curr_even = even_pre + odd_post[i]
            curr_odd = odd_pre + even_post[i]

            if i % 2:
                odd_pre += nums[i]
                curr_even -= nums[i]
            else:
                even_pre += nums[i]
                curr_odd -= nums[i]

            if curr_even == curr_odd:
                res += 1

        return res
