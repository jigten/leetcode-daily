from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        pre_sum, nz_cnt, pre_dig = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        pw_10 = [1] * (n + 1)

        for i in range(1, n):
            pw_10[i] = (pw_10[i - 1] * 10) % MOD

        if s[0] != "0":
            pre_sum[1] = int(s[0])
            nz_cnt[1] = 1
            pre_dig[1] = int(s[0])

        for i in range(1, n):
            c = s[i]
            if c == "0":
                pre_sum[i + 1] = pre_sum[i]
                nz_cnt[i + 1] = nz_cnt[i]
                pre_dig[i + 1] = pre_dig[i]
            else:
                pre_sum[i + 1] = int(c) + pre_sum[i]
                nz_cnt[i + 1] = 1 + nz_cnt[i]
                pre_dig[i + 1] = (pre_dig[i] * 10 + int(c)) % MOD

        res = []

        for ql, qr in queries:
            sum_ = pre_sum[qr + 1] - pre_sum[ql]
            cnt = nz_cnt[qr + 1] - nz_cnt[ql]
            dig = pre_dig[qr + 1] - pre_dig[ql] * pw_10[cnt]

            res.append((sum_ * dig) % MOD)

        return res
