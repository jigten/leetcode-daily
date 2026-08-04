import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res, day, h = 0, 1, []

        for i, (a, d) in enumerate(zip(apples, days)):
            heapq.heappush(h, (i + d, a))

            while h and h[0][0] < day:
                heapq.heappop(h)

            if h:
                ed, a_cnt = heapq.heappop(h)
                res += 1
                if a_cnt > 1:
                    heapq.heappush(h, (ed, a_cnt - 1))
            day += 1

        while h:
            while h and h[0][0] < day:
                heapq.heappop(h)

            if not h:
                break

            ed, a_cnt = heapq.heappop(h)

            res += 1
            if a_cnt > 1:
                heapq.heappush(h, (ed, a_cnt - 1))
            day += 1

        return res
