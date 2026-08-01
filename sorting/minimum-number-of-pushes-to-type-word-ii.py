from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        res = 0
        i = 0

        for cnt in sorted(counts.values(), reverse=True):
            res += cnt * ((i // 8) + 1)
            i += 1

        return res
