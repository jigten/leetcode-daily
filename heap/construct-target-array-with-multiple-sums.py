import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        S = sum(target)
        h = [-t for t in target]
        heapq.heapify(h)

        while h:
            x = heapq.heappop(h)
            x = abs(x)

            if x == 1:
                return True

            rest = S - x
            if x <= rest:
                return False

            prev = x - rest

            if prev == 0:
                prev = rest

            S = S - x + prev

            heapq.heappush(h, -prev)

        return False
