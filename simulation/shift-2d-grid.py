from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k:
            return grid

        m, n = len(grid), len(grid[0])
        total = m * n

        k %= total

        if not k:
            return grid

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_idx = (i * n) + j  # old idx in 1d array
                new_idx = (old_idx + k) % total  # new idx in 1d array after rotation

                new_i, new_j = (
                    new_idx // n,
                    new_idx % n,
                )  # back to 2d array after rotation
                res[new_i][new_j] = grid[i][j]

        return res

        curr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr[i][j] = grid[i][j]

        for _ in range(k):
            next_curr = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i < m - 1 and j == n - 1:
                        next_curr[i + 1][0] = curr[i][j]

                    elif i == m - 1 and j == n - 1:
                        next_curr[0][0] = curr[i][j]

                    else:
                        next_curr[i][j + 1] = curr[i][j]

            curr = next_curr

        return curr
