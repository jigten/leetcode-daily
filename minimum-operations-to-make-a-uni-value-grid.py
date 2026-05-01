from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([n for row in grid for n in row])
        n = len(nums)

        sentinel = nums[0] % x

        for i in range(1, n):
            if nums[i] % x != sentinel:
                return -1

        median = nums[n // 2]

        return sum(abs(val - median) for val in nums) // x

solution = Solution()
assert(solution.minOperations(grid = [[2,4],[6,8]], x = 2) == 4)
assert(solution.minOperations(grid = [[1,5],[2,3]], x = 1) == 5)
assert(solution.minOperations(grid = [[1,2],[3,4]], x = 2) == -1)
        