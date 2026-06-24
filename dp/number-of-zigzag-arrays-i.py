from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = (10 ** 9 + 7)
        M = r - l + 1
        dp = [[[0] * M for _ in range(2)] for _ in range(n)]

        # base case
        for v in range(M):
            dp[0][0][v] = 1
            dp[0][1][v] = 1
        

        for i in range(1, n):
            pref = list(accumulate(dp[i - 1][0]))
            suff = list(accumulate(dp[i - 1][1][::-1]))[::-1]
            for v in range(M):
                if v < M - 1: 
                    dp[i][0][v] += suff[v + 1] % MOD

                if v > 0:
                    dp[i][1][v] += pref[v - 1] % MOD
        
        return sum(dp[n - 1][d][v] for d in range(2) for v in range(M)) % MOD
