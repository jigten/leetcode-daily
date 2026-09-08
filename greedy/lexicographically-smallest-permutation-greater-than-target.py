from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(target)
        s_counts = Counter(s)

        def construct(p):
            need = [0] * 26
            bump = ""
            # calculate prefix we need to satisfy
            for i in range(p):
                need[(ord(target[i]) - ord("a"))] += 1

            # see if we can even satisfy the prefix
            for c in range(26):
                if need[c] > s_counts[chr(c + ord("a"))]:
                    return None

            # if we can satisfy the prefix, we now calculate the next best character we can insert as bump after the prefix
            for c in range(ord(target[p]) - ord("a") + 1, 26):
                if s_counts[chr(c + ord("a"))] - need[c] > 0:
                    bump = c
                    break
            else:
                return None

            # construct final string by taking prefix we can satisfy, the bump character, and the rest of the remaining characters in s in ascending order
            res = list(target[:p])
            res.append(chr(bump + ord("a")))
            for c in range(26):
                res.append(
                    chr(c + ord("a"))
                    * (s_counts[chr(c + ord("a"))] - need[c] - (1 if c == bump else 0))
                )

            return "".join(res)

        for p in range(n - 1, -1, -1):

            res = construct(p)

            if res:
                return res

        return ""
