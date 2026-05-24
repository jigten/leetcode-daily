from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(i):
            curr = 1
            for l in range(i - 1, max(i - d - 1, -1), -1):
                if arr[l] >= arr[i]:
                    break
                curr = max(curr, 1 + dfs(l))

            for r in range(i + 1, min(i + d + 1, len(arr))):
                if arr[r] >= arr[i]:
                    break
                curr = max(curr, 1 + dfs(r))

            return curr

        return max(dfs(i) for i in range(len(arr)))
