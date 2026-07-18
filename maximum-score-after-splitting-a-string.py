class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        res = 0

        # o(n) solution
        l_score = 1 if s[0] == "0" else 0
        r_score = 0

        for i in range(1, n):
            if s[i] == "1":
                r_score += 1

        for i in range(1, n):
            res = max(res, l_score + r_score)
            if s[i] == "0":
                l_score += 1

            if s[i] == "1":
                r_score -= 1

        return res

        # o(n ^ 2) solution
        for i in range(1, n):
            l_score, r_score = 0, 0

            for l in range(min(i + 1, n)):
                if s[l] == "0":
                    l_score += 1

            for r in range(i + 1, n):
                if s[r] == "1":
                    r_score += 1

            res = max(res, l_score + r_score)

        return res
