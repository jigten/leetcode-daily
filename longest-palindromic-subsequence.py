from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] == s[j]:
                return dp(i + 1, j - 1) + 2
            else:
                return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, n - 1)
