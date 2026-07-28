from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        first, middle = "", ""
        counts = Counter(s)

        for ch in sorted(counts):
            cnt = counts[ch]
            half = cnt // 2
            first += ch * half

            if cnt % 2 and not middle:
                middle = ch

        return first + middle + first[::-1]
