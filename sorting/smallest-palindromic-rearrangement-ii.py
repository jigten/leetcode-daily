from collections import Counter
from math import comb


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)

        left = {}
        middle = ""
        for ch in sorted(counts):
            cnt = counts[ch]
            half = cnt // 2
            if half:
                left[ch] = half
            if cnt % 2:
                middle = ch

        n = sum(left.values())

        if n == 0:
            return middle if k == 1 else ""

        P = 1
        remaining = n
        for cnt in left.values():
            P *= comb(remaining, cnt)
            remaining -= cnt

        if P < k:
            return ""

        res = []
        total = n
        left_copy = left.copy()

        while total > 0:
            for ch in sorted(left_copy):
                cnt = left_copy[ch]
                if cnt == 0:
                    continue
                block = P * cnt // total
                if k <= block:
                    res.append(ch)
                    left_copy[ch] -= 1
                    P = block
                    total -= 1
                    break
                k -= block

        left_str = "".join(res)
        return left_str + middle + left_str[::-1]
