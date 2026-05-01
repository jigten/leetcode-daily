from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = m - k + 1
        cols = n - k + 1
        if rows <= 0 or cols <= 0:
            return []

        res: List[List[int]] = []
        for r in range(rows):
            row_res: List[int] = []
            for c in range(cols):
                vals: List[int] = []
                for ri in range(r, r + k):
                    vals.extend(grid[ri][c:c + k])
                # only consider unique values per statement examples
                vals = sorted(set(vals))
                if len(vals) <= 1:
                    row_res.append(0)
                    continue
                min_diff = 10 ** 18
                for i in range(len(vals) - 1):
                    d = vals[i + 1] - vals[i]
                    if d < min_diff:
                        min_diff = d
                        if min_diff == 0:
                            break
                row_res.append(0 if min_diff == 10 ** 18 else min_diff)
            res.append(row_res)
        return res
