from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        costs.sort()

        for c in costs:
            if c <= coins:
                coins -= c
                res += 1
            else:
                break

        return res
