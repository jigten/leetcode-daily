from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        removed = 0

        for i in range(n):
            a, b = intervals[i]

            for j in range(n):
                if i == j:
                    continue

                c, d = intervals[j]

                if c <= a and b <= d:
                    removed += 1

        return n - removed

        intervals.sort(key=lambda x: x[0])
        ps, pe = intervals[0], intervals[1]

        for i in range(1, n):
            cs, ce = intervals[i]

        return n - removed
