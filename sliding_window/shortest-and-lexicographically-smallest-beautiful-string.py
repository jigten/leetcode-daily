class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        cnt, l = 0, 0
        ans = s

        for r, c in enumerate(s):
            cnt += int(c)

            while s[l] == "0" or cnt > k:
                cnt -= int(s[l])
                l += 1

            if cnt == k:
                t = s[l : r + 1]

                if len(t) < len(ans) or len(ans) == len(t) and t < ans:
                    ans = t

        return ans
