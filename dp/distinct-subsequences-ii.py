class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end = [0] * 26
        total = 1

        for c in s:
            key = ord(c) - ord("a")
            new_total = (total * 2 - end[key]) % MOD
            end[key] = total
            total = new_total

        return (total - 1) % MOD
