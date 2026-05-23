from typing import List


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 0

        for i in range(1, n):
            if i >= minJump:
                if dp[i - minJump]:
                    cnt += 1

            if i > maxJump:
                if dp[i - maxJump - 1]:
                    cnt -= 1

            if s[i] == '0' and cnt > 0:
                dp[i] = True

        return dp[-1]
