class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0] * 3
        l, r = 0, 0
        res = 0

        while r < len(s):
            freq[ord(s[r]) - ord("a")] += 1

            while all(c > 0 for c in freq):
                res += r - l + 1

                freq[ord(s[l]) - ord("a")] -= 1
                l += 1

            r += 1

        return res
