from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        if sum(v % 2 for v in counts.values()) > 1:
            return ""

        n = len(s)

        th = target[: n // 2]
        half_counts = {k: v // 2 for k, v in counts.items() if v // 2 > 0}
        mid = ""

        for k, v in counts.items():
            if v % 2:
                mid = k

        # if the firsth half of target matches our palindrome first half and if adding mid + tail of palindrome is greater than target that is the best we can do
        if Counter(th) == half_counts and th + mid + th[::-1] > target:
            return th + mid + th[::-1]

        def construct(p):
            need = [0] * 26

            for i in range(p):
                need[ord(th[i]) - ord("a")] += 1

            for c in range(26):
                if need[c] > half_counts.get(chr(c + ord("a")), 0):
                    return None

            bump = ""

            for c in range(ord(th[p]) - ord("a") + 1, 26):
                if half_counts.get(chr(c + ord("a")), 0) - need[c] > 0:
                    bump = c
                    break
            else:
                return None

            res = list(th[:p])

            res.append(chr(bump + ord("a")))
            for c in range(26):
                res.append(
                    chr(c + ord("a"))
                    * (
                        half_counts.get(chr(c + ord("a")), 0)
                        - need[c]
                        - (1 if c == bump else 0)
                    )
                )

            return "".join(res)

        # else we have reduced the problem to finding smallest lexicographically greater permutation of first half of target with first half of s
        for p in range(n // 2 - 1, -1, -1):
            res = construct(p)

            if res:
                return res + mid + res[::-1]

        return ""
