from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]

        loops = min(rows, cols) // 2

        for l in range(loops):
            curr_loop = []

            # get top
            for c in range(l, cols - l):
                curr_loop.append(grid[l][c])

            # get right col
            for r in range(l + 1, rows - l - 1):
                curr_loop.append(grid[r][cols - l - 1])

            # get bottom
            for c in range(cols - l - 1, l, -1):
                curr_loop.append(grid[rows - l - 1][c])

            # get left col
            for r in range(rows - l - 1, l, -1):
                curr_loop.append(grid[r][l])

            rotate = k % len(curr_loop)
            curr_loop = curr_loop[rotate:] + curr_loop[:rotate]

            idx = 0

            # assign top
            for c in range(l, cols - l):
                res[l][c] = curr_loop[idx]
                idx += 1

            # assign right col
            for r in range(l + 1, rows - l - 1):
                res[r][cols - l - 1] = curr_loop[idx]
                idx += 1

            # assign bottom
            for c in range(cols - l - 1, l, -1):
                res[rows - l - 1][c] = curr_loop[idx]
                idx += 1

            # assign left col
            for r in range(rows - l - 1, l, -1):
                res[r][l] = curr_loop[idx]
                idx += 1

        return res
