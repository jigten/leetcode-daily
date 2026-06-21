from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if nums1[r] == nums2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]

        return max(max(row) for row in dp)
