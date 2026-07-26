from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(s * s for _, _, s in squares)

        def calculateAreaBelow(l):
            area = 0.0

            for _, y, s in squares:
                if y >= l:
                    continue
                elif y + s < l:
                    area += s * s
                else:
                    area += s * (l - y)

            return area

        d, u = 0.0, float(max(y + s for _, y, s in squares))

        for _ in range(100):
            m = d + (u - d) / 2

            if calculateAreaBelow(m) >= total_area / 2:
                u = m
            else:
                d = m

        return d
