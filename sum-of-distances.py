from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idxs = defaultdict(list)
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            idxs[n].append(i)
        
        for i_arr in idxs.values():
            k = len(i_arr)
            if k == 1:
                continue
            
            total = sum(i_arr)
            left, right = 0, total

            for i, idx in enumerate(i_arr):
                right -= idx

                num_left = i
                num_right = k - i - 1

                left_dist = (num_left * idx) - left
                right_dist = right - (num_right * idx)

                res[idx] = left_dist + right_dist
      
                left += idx

        return res



solution = Solution()
assert(solution.distance(nums = [1,3,1,1,2]) == [5,0,3,4,0])
assert(solution.distance(nums = [0,5,3]) == [0,0,0])
        