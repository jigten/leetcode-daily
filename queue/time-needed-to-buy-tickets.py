from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res, i = 0, 0
        tq = deque((t, i) for i, t in enumerate(tickets))

        while tq:
            t, i = tq.popleft()

            res += 1
            t -= 1

            if i == k and t == 0:
                return res

            if t > 0:
                tq.append((t, i))

        return -1
