from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        prefs = [[0] * n for _ in range(m)]
        prefsX = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                curr = 0
                if grid[r][c] == 'X':
                    curr = 1

                if grid[r][c] == 'Y':
                    curr = -1

                if r > 0:
                    curr += prefs[r - 1][c]

                if c > 0:
                    curr += prefs[r][c - 1]

                if r > 0 and c > 0:
                    curr -= prefs[r - 1][c - 1]

                prefs[r][c] = curr

                xval = 1 if grid[r][c] == 'X' else 0
                xpref = xval
                if r > 0:
                    xpref += prefsX[r - 1][c]
                if c > 0:
                    xpref += prefsX[r][c - 1]
                if r > 0 and c > 0:
                    xpref -= prefsX[r - 1][c - 1]
                prefsX[r][c] = xpref

                if curr == 0 and prefsX[r][c] > 0:
                    res += 1
                
        return res
        