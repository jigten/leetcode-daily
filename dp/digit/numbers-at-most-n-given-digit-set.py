from typing import List
from functools import lru_cache


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)

        def findIdx(num):
            l, r = 0, len(digits) - 1
            res = -1

            while l <= r:
                m = l + (r - l) // 2
                mval = int(digits[m])

                if mval <= num:
                    res = m
                    l = m + 1
                else:
                    r = m - 1

            return res + 1

        @lru_cache(None)
        def dfs(i, is_tight):
            if i == len(n_str):
                return 1

            total = 0
            limit = 9
            if is_tight:
                limit = int(n_str[i])

            for j in range(min(len(digits), findIdx(limit))):
                current_digit = int(digits[j])
                next_tight = is_tight and (current_digit == limit)
                total += dfs(i + 1, next_tight)

            return total

        cnts = sum(len(digits) ** x for x in range(1, len(n_str)))

        return dfs(0, True) + cnts
