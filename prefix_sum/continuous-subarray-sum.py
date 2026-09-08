from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0: -1}
        pref_sum = 0

        for i, n in enumerate(nums):
            pref_sum += n
            rem = pref_sum % k

            if rem in rem_map:
                if i - rem_map[rem] >= 2:
                    return True
            else:
                rem_map[rem] = i

        return False
