import math
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(set(coins))
        coins = [
            x for i, x in enumerate(coins) if not any(x % y == 0 for y in coins[:i])
        ]
        n = len(coins)
        terms = []
        hi = coins[0] * k

        def build(idx, l, sign):
            for i in range(idx, n):
                nl = math.lcm(l, coins[i])
                if nl > hi:
                    continue
                terms.append((sign, nl))

                build(i + 1, nl, -sign)

        build(0, 1, 1)

        def count(X):
            return sum(s * (X // l) for s, l in terms)

        l, r = 0, coins[0] * k + 1

        while l < r:
            mid = l + (r - l) // 2

            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
