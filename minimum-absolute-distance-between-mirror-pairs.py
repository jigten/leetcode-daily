from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        INF = float('inf')
        res = INF
        seen = {}

        def reverse(num: int) -> int:
            return int(str(num)[::-1])

        for i, num in enumerate(nums):
            reversed = reverse(num)
            if num in seen:
                res = min(res, i - seen[num])

            seen[reversed] = i

        return -1 if res == INF else res

solution = Solution()
assert(solution.minMirrorPairDistance(nums = [12,21,45,33,54]) == 1)
assert(solution.minMirrorPairDistance(nums = [120,21]) == 1)
assert(solution.minMirrorPairDistance(nums = [21,120]) == -1)