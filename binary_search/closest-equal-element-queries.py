from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        vals_to_idx = defaultdict(list)

        for i, num in enumerate(nums):
            vals_to_idx[num].append(i)
        
        def getCircularDist(i, j):
            right_dist = abs(i - j)
            return min(right_dist, len(nums) - right_dist)

        for q in queries:
            curr = nums[q]
            idxs = vals_to_idx[curr]
            
            if len(idxs) == 1:
                res.append(-1)
                continue

            i = bisect.bisect_left(idxs, q)
            closest_left, closest_right = idxs[i - 1], idxs[(i + 1) % len(idxs)]

            res.append(min(getCircularDist(q, closest_left), getCircularDist(q, closest_right)))
  
        return res


solution = Solution()
assert(solution.solveQueries(nums = [1,3,1,4,1,3,2], queries = [0,3,5]) == [2,-1,3])
assert(solution.solveQueries(nums = [1,2,3,4], queries = [0,1,2,3]) == [-1,-1,-1,-1])