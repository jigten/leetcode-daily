from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pre = [0] * (2 * n + 1)
        pre[n] = 1
        cnt = n
        presum = res = 0

        for nu in nums:
            if nu == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1

            res += presum

        return res
