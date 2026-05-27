class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        idxs = {}
        seen = set()

        for i, c in enumerate(word):
            if c.islower():
                idxs[c] = i
            elif c not in idxs:
                idxs[c] = i

        for i, c in enumerate(word):
            if (
                c.isupper()
                and c not in seen
                and c.lower() in idxs
                and idxs[c.lower()] < idxs[c]
            ):
                res += 1
                seen.add(c)

        return res
